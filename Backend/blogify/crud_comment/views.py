from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Comment
from datetime import datetime
import json

# Créer un commentaire via JSON (ex: content + author_id)
@csrf_exempt
@require_http_methods(["POST"])
def create_comment(request, article_id):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponse("Invalid JSON", status=400)

    content = data.get('content')
    auteur = data.get('author_id')

    if content and auteur:
        new_comment = Comment(
            content=content,
            article_id=article_id,
            author_id=auteur,
            created_at=datetime.now()
        )
        new_comment.save()
        return HttpResponse("Comment created successfully")
    else:
        return HttpResponse("Invalid data", status=400)


# Mettre à jour un commentaire
@csrf_exempt
@require_http_methods(["POST"])
def update_comment(request, comment_id):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponse("Invalid JSON", status=400)

    content = data.get('content')

    if content:
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.content = content
            comment.save()
            return HttpResponse("Comment updated successfully")
        except Comment.DoesNotExist:
            return HttpResponse("Comment not found", status=404)
    else:
        return HttpResponse("Invalid data", status=400)


# Supprimer un commentaire
@csrf_exempt
@require_http_methods(["DELETE", "POST"])  # Supporte DELETE pur ou POST fallback
def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return HttpResponse("Comment deleted successfully")
    except Comment.DoesNotExist:
        return HttpResponse("Comment not found", status=404)


# Récupérer les commentaires d’un article (GET)
@require_http_methods(["GET"])
def get_comments(request, article_id):
    comments = Comment.objects.filter(article_id=article_id)
    comments_list = []

    for comment in comments:
        comments_list.append({
            'id': comment.id,
            'content': comment.content,
            'created_at': comment.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'author': comment.author.username
        })

    return JsonResponse(comments_list, safe=False)
