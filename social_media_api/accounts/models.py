from django.db import models
from social_media_api import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True, null=True)
    # followers: users who follow *this* user
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follower_set', blank=True)
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following_set",
        blank=True
    )

    def __str__(self):
        return self.username
    def follow(self, user):
        """Follow another user"""
        if user != self:
            self.following.add(user)

    def unfollow(self, user):
        """Unfollow another user"""
        if user != self:
            self.following.remove(user)

    def is_following(self, user):
        return self.following.filter(id=user.id).exists()

    def is_followed_by(self, user):
        return self.follower_set.filter(id=user.id).exists()
