from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name