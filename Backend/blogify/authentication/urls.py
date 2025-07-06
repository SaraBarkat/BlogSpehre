from django.urls import path
from .views import register_user, login_user,logout_view, update_profil, get_profil,author_settings

urlpatterns = [
    path('auth/register/', register_user),
    path('auth/login/', login_user),
    path('auth/logout/', logout_view),
    path('update_profile/<int:user_id>/', update_profil),
    path('get_profile/<int:user_id>/', get_profil),
    path('author/<int:author_id>/settings/', author_settings, name='settings'),

]
