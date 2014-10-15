from django.conf.urls import patterns, url
from portfolio import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^gallery$', views.gallery, name='gallery'),
  url(r'^music$', views.music, name='music'),
  url(r'^about$', views.about, name='about'),
)