from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:article_id>/', views.create_comment),
    path('<int:article_id>/', views.get_comments),
    path('<int:comment_id>/update/', views.update_comment),
    path('<int:comment_id>/delete/', views.delete_comment),
]
