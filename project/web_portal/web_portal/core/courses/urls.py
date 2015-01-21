from django.conf.urls import patterns, url

from .views import course_list, course_page, assignment_page, solution_page, \
    attend_course, attendee_solutions, add_course, add_assignment, \
    add_solution, delete_course

urlpatterns = patterns('',
    # Get urls
    url(r'^courses/$',
        course_list, name='course_list'),
    url(r'^courses/(?P<course_id>\d+)/$',
        course_page, name='course_page'),
    url(r'^courses/(?P<course_id>\d+)/assignments/(?P<assignment_id>\d+)/$',
        assignment_page, name='assignment_page'),
    url(r'^courses/(?P<course_id>\d+)/assignments/(?P<assignment_id>\d+)/solutions/(?P<solution_id>\d+)/$',
        solution_page, name='solution_page'),
    # Attendee urls
    url(r'^courses/(?P<course_id>\d+)/attend/$',
        attend_course, name='attend_course'),
    url(r'^courses/(?P<course_id>\d+)/attendee/(?P<attendee_id>\d+)/solutions$',
        attendee_solutions, name='attendee_solutions'),
    # Create urls
    url(r'^courses/add/$',
        add_course, name='add_course'),
    url(r'^courses/(?P<course_id>\d+)/assignments/add/$',
        add_assignment, name='add_assignment'),
    url(r'^courses/(?P<course_id>\d+)/assignments/(?P<assignment_id>\d+)/solutions/$',
        add_solution, name='add_solution'),
    # Delete urls
    url(r'^courses/(?P<course_id>\d+)/delete/$',
        delete_course, name='delete_course'),

    # TODO implement
    # from .views import edit_course, delete_assignment, delete_solution
    # url(r'^courses/(?P<pk>\d+)/edit/$', edit_course, name='edit_course'),
    # url(r'^courses/(?P<pk>\d+)/assignments/(?P<apk>\d+)/delete/$', delete_assignment, name='delete_assignment'),
    # url(r'^courses/(?P<pk>\d+)/assignments/(?P<apk>\d+)/solutions/(?P<spk>\d+)/delete/$', delete_solution, name='delete_solution'),
)