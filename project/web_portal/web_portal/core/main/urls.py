from django.conf.urls import patterns, url
from web_portal.core.main.views import coming, index

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^index$', index, name='index'),
    url(r'^coming$', coming, name='coming'),
)