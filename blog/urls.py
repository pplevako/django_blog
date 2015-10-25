from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new$', views.article_new, name='article-new'),
]