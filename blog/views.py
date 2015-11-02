from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from blog.forms import ArticleForm, CommentForm
from blog.models import Article, Comment


class ArticleMixin(object):
    model = Article
    form_class = ArticleForm  # also one can use fields = ['title', 'text']


class IndexView(ArticleMixin, generic.ListView):
    template_name = 'blog/articles/article_list.html'
    # context_object_name = 'article_list'


# class ArticleDetailView(ArticleMixin, generic.DetailView):
#     pass


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect(article)
    return render(request, 'blog/articles/article_detail.html', {'form': form, 'object': article})


class ArticleCreateView(ArticleMixin, generic.CreateView):
    template_name = 'blog/articles/article_new.html'


def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('blog:index')

    return render(request, 'blog/articles/article_edit.html', {'form': form})


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('blog:index')

    return render(request, 'blog/articles/article_confirm_delete.html', {'object': article})


def comment_delete(request, article_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        comment.delete()
        return redirect(article)

    return render(request, 'blog/articles/article_confirm_delete.html', {'object': comment})
