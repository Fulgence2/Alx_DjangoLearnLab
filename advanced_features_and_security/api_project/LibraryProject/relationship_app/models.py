from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    def __str__(self):
        return self.username  # AbstractUser already includes username


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
    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
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
