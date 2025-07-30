from django.conf import settings
from django.db import models

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
        ]

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

