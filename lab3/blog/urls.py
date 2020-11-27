from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('change-password',auth_views.PasswordChangeView.as_view(template_name='blog/change-password.html',success_url='/'),name='change-password'),
    path('logout',views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]