from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='users-register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'Users/login.html'), name="users-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'Users/logout.html'), name="users-logout"),
    path('profile/', views.profile, name='users-profile'),
    path('', views.re_home)
]