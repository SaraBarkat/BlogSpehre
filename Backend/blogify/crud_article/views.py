from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Article, Auteur
import json
from django.utils.dateparse import parse_datetime

@csrf_exempt
def create_article(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            author = Auteur.objects.get(id=data['author_id'])
            article = Article.objects.create(
                title=data['title'],
                content=data.get('content'),
                image_url=data.get('image_url'),
                published=data.get('published', 0),
                created_at=parse_datetime(data.get('created_at')),
                author=author
            )
            return JsonResponse({'id': article.id, 'message': 'Article créé avec succès'})
        except Auteur.DoesNotExist:
            return JsonResponse({'error': 'Auteur introuvable'}, status=404)
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

def list_articles(request):
    articles = Article.objects.all().values()
    return JsonResponse(list(articles), safe=False)

def get_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        return JsonResponse({
            'id': article.id,
            'title': article.title,
            'content': article.content,
            'image_url': article.image_url,
            'published': article.published,
            'created_at': article.created_at,
            'author_id': article.author.id
        })
    except Article.DoesNotExist:
        return HttpResponseNotFound('Article introuvable')

@csrf_exempt
def update_article(request, article_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            article = Article.objects.get(id=article_id)
            article.title = data.get('title', article.title)
            article.content = data.get('content', article.content)
            article.image_url = data.get('image_url', article.image_url)
            article.published = data.get('published', article.published)
            article.created_at = parse_datetime(data.get('created_at')) or article.created_at
            article.save()
            return JsonResponse({'message': 'Article mis à jour'})
        except Article.DoesNotExist:
            return HttpResponseNotFound('Article introuvable')
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

@csrf_exempt
def delete_article(request, article_id):
    if request.method == 'DELETE':
        try:
            article = Article.objects.get(id=article_id)
            article.delete()
            return JsonResponse({'message': 'Article supprimé'})
        except Article.DoesNotExist:
            return HttpResponseNotFound('Article introuvable')
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
