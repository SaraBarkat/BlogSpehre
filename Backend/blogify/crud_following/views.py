from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Follows
from crud_article.models import Auteur
from datetime import datetime
import json

#  Créer une relation de "follow"
@csrf_exempt
@require_http_methods(["POST"])
def create_follow(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponse("Invalid JSON", status=400)

    following_id = data.get('following_user_id')
    followed_id = data.get('followed_user_id')

    if following_id and followed_id and following_id != followed_id:
        try:
            follower = Auteur.objects.get(id=following_id)
            followed = Auteur.objects.get(id=followed_id)

            follow, created = Follows.objects.get_or_create(
                following_user=follower,
                followed_user=followed,
                defaults={'created_at': datetime.now()}
            )

            if created:
                return HttpResponse("Follow created successfully")
            else:
                return HttpResponse("Follow already exists", status=200)

        except Auteur.DoesNotExist:
            return HttpResponse("Invalid author IDs", status=404)
    else:
        return HttpResponse("Invalid data", status=400)


# supprimer un follow
@csrf_exempt
@require_http_methods(["DELETE", "POST"])  # autorise DELETE ou POST
def delete_follow(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponse("Invalid JSON", status=400)

    following_id = data.get('following_user_id')
    followed_id = data.get('followed_user_id')

    if following_id and followed_id:
        try:
            Follows.objects.get(
                following_user_id=following_id,
                followed_user_id=followed_id
            ).delete()
            return HttpResponse("Follow deleted successfully")
        except Follows.DoesNotExist:
            return HttpResponse("Follow not found", status=404)
    else:
        return HttpResponse("Invalid data", status=400)


#  Obtenir les auteurs suivis par un utilisateur
@require_http_methods(["GET"])
def get_following(request, user_id):
    follows = Follows.objects.filter(following_user_id=user_id)
    result = [{
        'followed_user_id': f.followed_user.id,
        'followed_username': f.followed_user.username,
        'created_at': f.created_at.strftime("%Y-%m-%d %H:%M:%S") if f.created_at else None
    } for f in follows]

    return JsonResponse(result, safe=False)


#  Obtenir les abonnés d’un utilisateur
@require_http_methods(["GET"])
def get_followers(request, user_id):
    follows = Follows.objects.filter(followed_user_id=user_id)
    result = [{
        'follower_id': f.following_user.id,
        'follower_username': f.following_user.username,
        'created_at': f.created_at.strftime("%Y-%m-%d %H:%M:%S") if f.created_at else None
    } for f in follows]

    return JsonResponse(result, safe=False)
