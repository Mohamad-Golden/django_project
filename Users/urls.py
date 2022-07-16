from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PasswordChange, PasswordReset


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='users-register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'Users/login.html'), name="users-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'Users/logout.html'), name="users-logout"),
    path('profile/', views.profile, name='users-profile'),
    path('', views.re_home),
    path('chpassword/', PasswordChange.as_view(), name='chpassword'),
    path('password-reset/', PasswordReset.as_view(), name='password_reset'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='Users/password-reset-confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'Users/password-reset-complete.html'), name='password_reset_complete')
]