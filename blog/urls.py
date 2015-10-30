from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),  # rename to article-list?
    url(r'^new$', views.article_new, name='article-new'),
    # url(r'^(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='article-detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.article_detail, name='article-detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.article_edit, name='article-edit'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.article_delete, name='article-delete'),
    url(r'^(?P<article_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/delete$', views.comment_delete, name='comment-delete'),
]
