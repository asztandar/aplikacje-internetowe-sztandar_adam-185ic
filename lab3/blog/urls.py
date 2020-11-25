from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('logout',views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('change-password',auth_views.PasswordChangeView.as_view(template_name='blog/change-password.html',success_url='/'),name='change-password'),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='blog/password-reset/password_reset.html',
             subject_template_name='blog/password-reset/password_reset_subject.txt',
             email_template_name='blog/password-reset/password_reset_email.html',
             success_url='/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='blog/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='blog/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='blog/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]