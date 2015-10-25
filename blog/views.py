from django.shortcuts import render
from django.views import generic
from blog.forms import ArticleForm
from blog.models import Article


# Create your views here.
class IndexView(generic.ListView):
    model = Article
    # template_name = 'blog/article_list.html'
    # context_object_name = 'article_list'


def article_new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
    else:
        form = ArticleForm()

    return render(request, 'blog/article_new.html', {'form': form})

