from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import BlogLogoutView, BlogLoginView, register, profile

app_name = "blog"

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    # path('register/', views.register, name='register'),
    # path('profile/', views.profile, name='profile'),
    path("", BlogLogoutView.as_view(), name="logout"),
    path("login/", BlogLoginView.as_view(), name="login"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("logout/", BlogLogoutView.as_view(), name="logout"),
]
