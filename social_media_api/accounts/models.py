from django.db import models
from social_media_api import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True, null=True)
    # followers: users who follow *this* user
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following_set', blank=True)

    def __str__(self):
        return self.username
