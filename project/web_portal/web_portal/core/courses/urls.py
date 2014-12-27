from django.conf.urls import patterns, url
from web_portal.core.courses.views import course_list, add_course, edit_course, delete_course, course_page

urlpatterns = patterns('',
    url(r'^courses/$', course_list, name = 'course_list'),
    url(r'^course/add/$', add_course, name = 'add_course'),
    url(r'^course/(?P<pk>\d+)/$', course_page, name = 'course_page'),
    url(r'^course/(?P<pk>\d+)/edit/$', edit_course, name = 'edit_course'),
    url(r'^course/(?P<pk>\d+)/delete$', delete_course, name='delete_course'),
)