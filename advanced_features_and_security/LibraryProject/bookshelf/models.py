from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class MyModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookshelf_mymodels'  # 👈 unique to bookshelf
    )
    class Meta:
        permissions = [
            ("can_create", "Can add book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
            ("can_view", "Can view book"),
        ]

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(
        null=True,
        blank=True,
        upload_to="profile_photos",
        default="profile_photos/default.jpg"
    )
    def __str__(self):
        return self.username
    class Meta:
        permissions = [
            ("can_create", "Can add book"),
            ("can_edit", "Can edit book"),
        ]

class CustomUserAdmin(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
    def _create_superuser(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )