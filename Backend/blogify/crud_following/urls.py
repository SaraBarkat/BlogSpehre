from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_follow),
    path('delete/', views.delete_follow),
    path('following/<int:user_id>/', views.get_following),
    path('followers/<int:user_id>/', views.get_followers),
]
