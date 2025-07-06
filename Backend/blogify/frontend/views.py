from django.shortcuts import render, get_object_or_404
from crud_article.models import Article,Auteur
from crud_comment.models import Comment
from django.shortcuts import  redirect
from django.contrib.auth import logout



def home(request):
    articles = Article.objects.all().order_by('-created_at')[:9] 
    return render(request, 'index.html', {'articles': articles})


def discover_view(request):
    query = request.GET.get('q', '')
    if query:
        articles = Article.objects.filter(title__icontains=query)
    else:
        articles = Article.objects.all().order_by('-created_at')[:20]
    return render(request, 'discover.html', {'articles': articles, 'query': query})


def login_view(request):
    return render(request, 'login.html')
def forgot_password_view(request):  
    return render(request, 'forgotPassword.html')

def register_view(request):
    return render(request, 'register.html')
def page_not_found_view(request):
    return render(request, '404.html')
def server_error_view(request):
    return render(request, '500.html')


def article_detail_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(article=article).order_by('-created_at')

    return render(request, 'AffichageArticle.html', {
        'article': article,
        'article_id': article_id,
        'comments': comments,
    })
   

def author_profil_view(request, author_id):
    author = get_object_or_404(Auteur, pk=author_id)
    articles = Article.objects.filter(author=author)
    return render(request, 'authorProfil.html', {'author': author, 'articles': articles})


def author_dashboard_view(request, author_id):
    author = get_object_or_404(Auteur, pk=author_id)
    articles = Article.objects.filter(author=author)
    return render(request, 'auteurDashboard.html', {'author': author, 'articles': articles})

def author_settings_view(request, author_id):
    author = get_object_or_404(Auteur, pk=author_id)
    articles = Article.objects.filter(author=author)
    return render(request, 'auteurSettings.html', {'author': author, 'articles': articles})


def article_create_view(request, author_id):
     author = get_object_or_404(Auteur, pk=author_id)
     return render(request, 'create_article.html', {'author': author})

def article_edit_view(request, article_id):
     article = get_object_or_404(Article, pk=article_id)
     return render(request, 'edit_article.html', {'article': article})

def logout_view(request):
    request.session.flush()
    return redirect('home')
 
# Uncomment the following lines if you have article creation, editing, or deletion views

# def article_edit_view(request, article_id):   
#     return render(request, 'articleEdit.html', {'article_id': article_id})
# def article_delete_view(request, article_id):
#     return render(request, 'articleDelete.html', {'article_id': article_id})
