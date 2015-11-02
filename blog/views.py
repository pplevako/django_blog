from django.core.urlresolvers import reverse_lazy
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


class ArticleUpdateView(ArticleMixin, generic.UpdateView):
    template_name = 'blog/articles/article_edit.html'


# def article_delete(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'POST':
#         article.delete()
#         return redirect('blog:index')
#
#     return render(request, 'blog/articles/article_confirm_delete.html', {'object': article})


class ArticleDeleteView(ArticleMixin, generic.DeleteView):
    template_name = 'blog/articles/article_confirm_delete.html'
    success_url = reverse_lazy('blog:index')  # or use get_success_url with a regular reverse


# def comment_delete(request, article_id, comment_id):
#     article = get_object_or_404(Article, pk=article_id)
#     comment = get_object_or_404(article.comment_set, pk=comment_id)
#     if request.method == 'POST':
#         comment.delete()
#         return redirect(article)
#
#     return render(request, 'blog/comments/comment_confirm_delete.html', {'object': comment})


class CommentDeleteView(generic.DeleteView):
    model = Comment
    template_name = 'blog/comments/comment_confirm_delete.html'
    pk_url_kwarg = 'comment_id'

    def get_queryset(self):
        article = get_object_or_404(Article, pk=self.kwargs['article_id'])
        return article.comment_set  # or Comment.objects.filter(article=article)

    def get_success_url(self):
        return self.object.article.get_absolute_url()
