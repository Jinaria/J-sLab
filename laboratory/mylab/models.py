from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True)
    category = models.CharField(max_length=40, default='diary')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.subject
    
class Comment(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:10] + '...'