from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField()


class Comment(models.Model):
    post = models.ForeignKey(Post)
    memssage = models.TextField()
