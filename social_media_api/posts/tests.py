from django.test import TestCase

from accounts.models import User
from posts.models import Post, Comment


# Create your tests here.

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            email="<EMAIL>",
            password="<PASSWORD>",
            first_name="test",
            last_name="test",
            role="test",
            is_active=True,
            is_superuser=True,
            is_staff=True,
        )
        self.post = Post.objects.create()
        self.post.author = self.user
        self.post.save()

class CommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            email="<EMAIL>",
            password="<PASSWORD>",
            first_name="test",
            last_name="test",
            role="test",
            is_active=True,
            is_superuser=True,
            is_staff=True,
        )
        self.comment = Comment.objects.create(
            author=self.user,
            content="This is a test comment",
        )