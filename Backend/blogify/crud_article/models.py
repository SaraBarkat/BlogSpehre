from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/images/', blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='articles')
    
    class Meta:
        permissions = [
            ("can_publish_article", "Can publish article"),
            ("can_edit_article", "Can edit article"),
        ]
