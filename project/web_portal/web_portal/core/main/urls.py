from django.conf.urls import patterns, url

from .views import coming, index

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^index$', index, name='index'),
    url(r'^coming$', coming, name='coming'),
)