from django.conf.urls import patterns, url

from .views import course_list, add_course, edit_course,\
    delete_course, course_page, add_assignment, assignment_page, delete_assignment,\
    attend_course, attendee_solutions, add_solution, solution_page, delete_solution

urlpatterns = patterns('',
    url(r'^courses/$', course_list, name='course_list'),
    url(r'^courses/add/$', add_course, name='add_course'),
    url(r'^courses/(?P<pk>\d+)/$', course_page, name='course_page'),
    url(r'^courses/(?P<pk>\d+)/edit/$', edit_course, name='edit_course'),
    url(r'^courses/(?P<pk>\d+)/delete/$', delete_course, name='delete_course'),
    url(r'^courses/(?P<pk>\d+)/attend/$', attend_course, name='attend_course'),
    url(r'^courses/(?P<pk>\d+)/attendee/(?P<apk>\d+)/solutions$', attendee_solutions, name='attendee_solutions'),

    url(r'^courses/(?P<pk>\d+)/assignments/add/$', add_assignment, name='add_assignment'),
    url(r'^courses/(?P<pk>\d+)/assignments/(?P<apk>\d+)/$', assignment_page, name='assignment_page'),
    url(r'^courses/(?P<pk>\d+)/assignments/(?P<apk>\d+)/delete/$', delete_assignment, name='delete_assignment'),
    url(r'^courses/(?P<pk>\d+)/assignments/(?P<apk>\d+)/solutions/$', add_solution, name='add_solution'),
    url(r'^courses/(?P<pk>\d+)/assignments/(?P<apk>\d+)/solutions/(?P<spk>\d+)/$', solution_page, name='solution_page'),
    url(r'^courses/(?P<pk>\d+)/assignments/(?P<apk>\d+)/solutions/(?P<spk>\d+)/delete/$', delete_solution, name='delete_solution'),
)