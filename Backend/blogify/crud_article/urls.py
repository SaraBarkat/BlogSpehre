from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_articles),
    path('create/', views.create_article),
    path('<int:article_id>/', views.get_article),
    path('<int:article_id>/update/', views.update_article),
    path('<int:article_id>/delete/', views.delete_article),
    path('articles/',views.list_articles) ,
]
