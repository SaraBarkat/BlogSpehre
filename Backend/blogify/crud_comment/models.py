from django.db import models
from crud_article.models import Article
from crud_article.models import Auteur

class Comment(models.Model):
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Auteur, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'comment'

