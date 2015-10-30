from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from blog.forms import ArticleForm, CommentForm
from blog.models import Article


# Create your views here.
class IndexView(generic.ListView):
    model = Article
    # template_name = 'blog/article_list.html'
    # context_object_name = 'article_list'


class ArticleDetailView(generic.DetailView):
    model = Article


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect(article)
    return render(request, 'blog/article_detail.html', {'form': form, 'object': article})


def article_new(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog:index')

    return render(request, 'blog/article_new.html', {'form': form})


def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('blog:index')

    return render(request, 'blog/article_edit.html', {'form': form})


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('blog:index')

    return render(request, 'blog/article_confirm_delete.html', {'object': article})
