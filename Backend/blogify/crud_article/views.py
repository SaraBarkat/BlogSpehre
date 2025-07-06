from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from .models import Article, Auteur
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.forms.models import model_to_dict
import json


@csrf_exempt
def create_article(request, author_id):
    if request.method == 'POST':
        title = request.POST.get('title')
        resume = request.POST.get('summary')
        categorie = request.POST.get('category')
        content = request.POST.get('content')
        image = request.FILES.get('cover_image')

        try:
            published = int(request.POST.get('published', 0))
        except ValueError:
            published = 0

        try:
            author = Auteur.objects.get(id=author_id)
            article = Article.objects.create(
                title=title,
                resume=resume,
                content=content,
                Categorie=categorie,
                image=image,
                published=published,
                created_at=now(),
                author=author
            )
            return redirect('author_dashboard', author_id=author.id)
        except Auteur.DoesNotExist:
            return render(request, '404.html')


def list_articles(request):
    articles = Article.objects.all()
    data = []

    for article in articles:
        item = model_to_dict(article)
        item['image'] = article.image.url if article.image else None
        item['author'] = {
            'id': article.author.id,
            'username': article.author.username,
            'first_name': article.author.first_name,
            'family_name': article.author.family_name,
        }
        data.append(item)

    return JsonResponse(data, safe=False)


def get_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        return JsonResponse({
            'id': article.id,
            'title': article.title,
            'resume': article.resume,
            'content': article.content,
            'Categorie': article.Categorie,
            'image': article.image.url if article.image else None,
            'published': article.published,
            'created_at': article.created_at,
            'author': {
                'id': article.author.id,
                'username': article.author.username,
                'first_name': article.author.first_name,
                'family_name': article.author.family_name,
            }
        })
    except Article.DoesNotExist:
        return render(request, '404.html')


@csrf_exempt
def update_article(request, article_id):
    if request.method == 'POST':
        try:
            article = Article.objects.get(id=article_id)
            article.title = request.POST.get('title', article.title)
            article.resume = request.POST.get('summary', article.resume)
            article.Categorie = request.POST.get('category', article.Categorie)
            article.content = request.POST.get('content', article.content)

            try:
                article.published = int(request.POST.get('published', article.published))
            except ValueError:
                pass

            if 'cover_image' in request.FILES:
                article.image = request.FILES['cover_image']

            article.save()
            return redirect('author_dashboard', author_id=article.author.id)

        except Article.DoesNotExist:
            return render(request, '404.html')
    return render(request, '404.html')


@csrf_exempt
def article_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('author_dashboard', author_id=article.author.id)


def discover(request):
    query = request.GET.get('q', '').strip()
    articles = []

    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(resume__icontains=query) |
            Q(Categorie__icontains=query) |
            Q(author__username__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__family_name__icontains=query)
        )

    return render(request, 'discover.html', {
        'articles': articles,
        'query': query
    })
