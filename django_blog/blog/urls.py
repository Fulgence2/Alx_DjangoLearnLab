from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import BlogLogoutView, BlogLoginView, register, profile, PostListView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView

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
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
