from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    image = models.ImageField(upload_to='posts_images/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return f'title:{self.title} \ content:{self.content}\ns'