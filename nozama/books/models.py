from django.db import models
from nozama.authors.models import Author


class Book(models.Model):
    name = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE())