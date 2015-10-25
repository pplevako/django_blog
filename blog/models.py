from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


class Comment(models.Model):
    article = models.ForeignKey(Article)
    commenter = models.CharField(max_length=200)
    text = models.TextField()

