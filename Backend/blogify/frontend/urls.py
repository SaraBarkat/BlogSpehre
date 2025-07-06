from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('forgot_password/', views.forgot_password_view, name='forgot_password'),
    path('register/', views.register_view, name='register'),
    path('logout',views.logout_view,name='logout'),
    path('404/', views.page_not_found_view, name='page_not_found'),
    path('500/', views.server_error_view, name='server_error'),
    path('article/<int:article_id>/', views.article_detail_view, name='article_detail'),
    path('discover/', views.discover_view, name='discover'),
    path('article_create/<int:author_id>/', views.article_create_view, name='create_article'),
    path('article_edit/<int:article_id>/', views.article_edit_view, name='article_edit'),
    path('Author_Dashboard/<int:author_id>/', views.author_dashboard_view, name='author_dashboard'),
    path('Author_Settings/<int:author_id>/', views.author_settings_view, name='author_settings'),
    path('author/<int:author_id>/', views.author_profil_view,name='author_profil')

    #path('article_delete/<int:article_id>/', views.article_delete_view, name='article_delete'),

]
