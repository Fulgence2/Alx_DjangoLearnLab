from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        permissions = (
            ("can_view_post", "Can view post"),
            ("can_edit_post", "Can edit post"),
            ("can_delete_post", "Can delete post"),
            ("can_manage_post", "Can manage post"),
        )
    def __str__(self):
        return f"{self.title} ({self.author})"

class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        related_query_name="comments",
        null=True,
        blank=True,
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        permissions = (
            ("can_view_comment", "Can view comment"),
            ("can_edit_comment", "Can edit comment"),
            ("can_delete_comment", "Can delete comment"),
            ("can_manage_comment", "Can manage comment"),
        )
    def __str__(self):
        return f"Comment by {self.author} on ({self.post})"

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post")  # prevent multiple likes by same user

    def __str__(self):
        return f"{self.user.username} likes {self.post.id}"