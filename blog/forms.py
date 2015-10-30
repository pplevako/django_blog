from django.forms import ModelForm
from blog.models import Article, Comment


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['commenter', 'text']
