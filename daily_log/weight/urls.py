from django.conf.urls import patterns, url

from weight import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^all.json$', views.alljson, name='alljson'),
)
