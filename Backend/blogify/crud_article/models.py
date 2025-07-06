# crud_article/models.py

from django.db import models
from django.utils import timezone

class Auteur(models.Model):
    username = models.CharField(max_length=255) 
    
    first_name = models.CharField(max_length=100, blank=True, null=True)
    family_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)  
    password = models.CharField(max_length=255, null=True, blank=True)  # stocké en hash
    role = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='auteurs/', blank=True, null=True) 
    bio = models.TextField(blank=True, null=True)  
    profession = models.TextField(blank=True, null=True,default='Author')
    class Meta:
        db_table = 'auteur'

    def __str__(self):
        return self.username



class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)   
    published = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(Auteur, on_delete=models.DO_NOTHING)
    Categorie= models.TextField(blank=True, null=True)
    class Meta:
        db_table = 'article'


