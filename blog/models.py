from django.core.urlresolvers import reverse
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    text = models.TextField()

    def __unicode__(self):  # __str__ on Python 3
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article-detail', args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(Article)
    commenter = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    text = models.TextField()
