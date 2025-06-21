from django.db import models
from crud_article.models import Auteur
class Follows(models.Model):
    following_user = models.OneToOneField(
        Auteur, primary_key=True, on_delete=models.DO_NOTHING, related_name='following_user'
    )
    followed_user = models.ForeignKey(
        Auteur, on_delete=models.DO_NOTHING, related_name='followed_user_set'
    )
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'follows'
        unique_together = (('following_user', 'followed_user'),)
