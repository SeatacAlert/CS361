from django.db import models


class URL(models.Model):
    original_url = models.URLField(unique=True)
    shortened_url = models.CharField(max_length=8, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url
