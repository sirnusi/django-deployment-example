from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='Images')

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=256)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    thumbnail = models.ImageField(default='PostImages')
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title
