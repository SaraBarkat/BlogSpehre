from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_articles),
    path('create/<int:author_id>', views.create_article),
    path('<int:article_id>/', views.get_article),
    path('update/<int:article_id>/', views.update_article),
    path('delete/<int:article_id>/', views.article_delete, name='article_delete'),
    path('articles/',views.list_articles) ,
    path('discover/', views.discover, name='discover'),

]
