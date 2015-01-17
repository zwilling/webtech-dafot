from django.conf.urls import patterns, url

from .views import coming, index, our_team

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^index$', index, name='index'),
    url(r'^our-team$', our_team, name='our_team'),
    url(r'^coming$', coming, name='coming'),
)