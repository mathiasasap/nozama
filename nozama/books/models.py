from django.db import models
from authors.models import Author


class Book(models.Model):
    name = models.CharField(max_length=48)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name