from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),  # rename to article-list?
    url(r'^new$', views.article_new, name='article-new'),
    url(r'^(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='article-detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.article_edit, name='article-edit'),
]
