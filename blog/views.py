from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
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
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('blog:index'))

    return render(request, 'blog/article_new.html', {'form': form})
