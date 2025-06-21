# crud_article/models.py

from django.db import models
from django.utils import timezone

class Auteur(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)  # nouveau
    password = models.CharField(max_length=255, null=True, blank=True)  # nouveau, stocké en hash
    role = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'auteur'

    def __str__(self):
        return self.username



class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    published = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(Auteur, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'article'


