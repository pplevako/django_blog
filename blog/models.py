from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __unicode__(self):  # __str__ on Python 3
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article)
    commenter = models.CharField(max_length=200)
    text = models.TextField()
