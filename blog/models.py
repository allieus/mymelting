from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    memssage = models.TextField()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.post_id])
