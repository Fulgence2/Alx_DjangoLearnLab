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
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    # Comment URLs
    path("post/<int:post_id>/comments/new/", add_comment, name="comment-add"),
    path("comments/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
