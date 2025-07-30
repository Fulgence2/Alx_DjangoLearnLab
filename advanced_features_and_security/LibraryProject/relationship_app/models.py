from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

class MyModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='relationship_mymodels'  # 👈 unique to relationship_app
    )

# Create your models here.
class Relationship(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author =models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        permissions = [
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE_CHOICES, max_length=20, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Automatically create UserProfile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username