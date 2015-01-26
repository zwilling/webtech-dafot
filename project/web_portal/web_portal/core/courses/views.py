import json
from collections import defaultdict

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST, require_GET

import api
from .forms import CourseForm, AssignmentForm, SolutionForm
from .utils import (clean_location, clean_solution, user_is_attendee,
                    user_is_organizer, get_page_from_request)


@require_GET
def course_list(request):
    """
    Course list view. Gets a list of courses, paginates and generates
    `courses/course_list.html` template as a response.

    :param request: :class:`Request` object
    :return: :class:`HttpResponse` object
    """
    page = get_page_from_request(request)
    courses = api.get_courses()
    paginator = Paginator(courses, 4)
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)
    return render(request, 'courses/course_list.html', {
        'courses': courses, 'paginator': paginator
    })


@require_GET
@login_required(login_url='/accounts/login/')
def course_page(request, course_id):
    """
    Course page view. Gets a course and generates `courses/course_page.html`
    template as a response.

    :param request: :class:`Request` object
    :param course_id: Id of the requested course
    :type course_id: int
    :return: :class:`HttpResponse` object
    """
    course_id = int(course_id)
    user = request.user
    user_credentials = (user.username, user.password)
    course = api.get_course(course_id, auth=user_credentials)
    params = {}
    organizer = course.courseOrganizer
    organizer_img = api.get_user_avatar_url(organizer.id)
    attendees = course.courseAttendees
    is_attendee = user_is_attendee(user, attendees)
    is_organizer = user_is_organizer(user, organizer)
    if is_attendee or is_organizer:
        params['assignments'] = api.get_assignments(course_id, auth=user_credentials)
        if is_organizer:
            params['attendees'] = attendees
            params['languages'] = [[l[0], l[1]] for l in settings.LANGUAGES]
    params.update({'course': course,
                   'organizer': organizer,
                   'organizer_img': organizer_img,
                   'is_attendee': is_attendee,
                   'is_organizer': is_organizer
    })
    return render(request, 'courses/course_page.html', params)


@login_required(login_url='/accounts/login/')
def assignment_page(request, course_id, assignment_id):
    """
    Assignment page view. Gets a course and generates `courses/assignment_page.html`
    template as a response.

    :param request: :class:`Request` object
    :param course_id: Id of the course to which requested assignment belongs
    :type course_id: int
    :param assignment_id: Id of the requested assignment
    :type assignment_id: int
    :return: :class:`HttpResponse` object
    """
    course_id = int(course_id)
    assignment_id = int(assignment_id)
    user = request.user
    user_credentials = (user.username, user.password)
    response = api.get_assignments(course_id, clipped_body=False, auth=user_credentials)
    assignments = response.assignment
    assignment = next((obj for obj in assignments if obj.id == assignment_id), None)
    is_organizer = user_is_organizer(user, response.course.courseOrganizer)
    params = {'course_id': course_id,
              'assignment': assignment,
              'assignments': assignments,
              'is_organizer': is_organizer}
    if not is_organizer:
        params['solutions'] = api.get_solutions(course_id, assignment_id, auth=user_credentials)
    return render(request, 'courses/assignment_page.html', params)


@require_GET
@login_required(login_url='/accounts/login/')
def solution_page(request, course_id, assignment_id, solution_id):
    """
    Solution page view. Gets a course and generates `courses/solution_page.html`
    template as a response.

    :param request: :class:`Request` object
    :param course_id: Id of the course to which requested solution belongs
    :type course_id: int
    :param assignment_id: Id of the assignment to which requested solution belongs
    :type assignment_id: int
    :param solution_id: Id of the requested solution
    :type solution_id: int
    :return: :class:`HttpResponse` object
    """
    course_id = int(course_id)
    assignment_id = int(assignment_id)
    solution_id = int(solution_id)
    user = request.user
    user_credentials = (user.username, user.password)
    assignments = api.get_assignments(course_id, auth=user_credentials)
    assignment = next((obj for obj in assignments if obj.id == assignment_id), None)
    solutions = api.get_solutions(course_id, assignment_id, auth=user_credentials)
    solution = next((obj for obj in solutions if obj.id == solution_id), None)
    params = {'assignments': assignments,
              'assignment': assignment,
              'curr_solution': solution,
              'solutions': solutions,
              'course_id': course_id}
    return render(request, 'courses/solution_page.html', params)


@require_POST
@login_required(login_url='/accounts/login/')
def add_course(request):
    """
    Add course view. Gets a data from the form and requests an API create a
    new course with this data.

    :param request: :class:`Request` object
    :raises: :class:`HttpResponseBadRequest`
    :return: :class:`HttpResponse` object
    """
    if request.is_ajax():
        form = CourseForm(request.POST)
        if form.is_valid():
            user_credentials = (request.user.username, request.user.password)
            json_data = {'name': form.cleaned_data['name'],
                    'description': form.cleaned_data['description']}
            location = api.create_course(json_data, auth=user_credentials)
            course_url = clean_location(location)
            return HttpResponse(json.dumps({'url': course_url}),
                                content_type="application/json", status=201)
    return HttpResponseBadRequest()


@require_POST
@login_required(login_url='/accounts/login/')
def add_assignment(request, course_id):
    """
    Add assignment view. Gets a data from the form and requests an API create a
    new assignment with this data in a course.

    :param request: :class:`Request` object
    :param course_id: Id of the course to create a new assignment in
    :type course_id: int
    :raises: :class:`HttpResponseBadRequest`
    :return: :class:`HttpResponse` object
    """
    course_id = int(course_id)
    if request.is_ajax():
        form = AssignmentForm(request.POST)
        if form.is_valid():
            user_credentials = (request.user.username, request.user.password)
            json_data = {
                'name': form.cleaned_data['name'],
                'description': form.cleaned_data['description'],
                'language': form.cleaned_data['language'],
                'templateCode': form.cleaned_data['template_code'],
                'verificationCode': form.cleaned_data['verification_code']
            }
            location = api.create_assignment(course_id, json_data, auth=user_credentials)
            assignment_url = clean_location(location)
            return HttpResponse(json.dumps({'url': assignment_url}),
                                content_type="application/json", status=201)
    return HttpResponseBadRequest()


@require_POST
@login_required(login_url='/accounts/login/')
def add_solution(request, course_id, assignment_id):
    """
    Add solution view. Gets a data from the form and requests an API create a
    new solution with this data in an assignment in the course.

    :param request: :class:`Request` object
    :param course_id: Id of the course to create a new solution in
    :type course_id: int
    :param assignment_id: Id of the assignment to create a new solution in
    :type assignment_id: int
    :raises: :class:`HttpResponseBadRequest`
    :return: :class:`HttpResponse` object
    """
    course_id = int(course_id)
    assignment_id = int(assignment_id)
    if request.is_ajax():
        form = SolutionForm(request.POST)
        if form.is_valid():
            user_credentials = (request.user.username, request.user.password)
            json_data = {'code': form.cleaned_data['code']}
            location = api.create_solution(course_id, assignment_id, json_data, auth=user_credentials)
            solution_url = clean_location(location)
            return HttpResponse(json.dumps({'url': solution_url}),
                                content_type="application/json", status=201)
    return HttpResponseBadRequest


@login_required(login_url='/accounts/login/')
def attend_course(request, course_id):
    """
    Attend course view. Requests an API to add a user to the course.

    :param request: :class:`Request` object
    :param course_id: Id of the course to add new user at
    :type course_id: int
    :raises: :class:`HttpResponseBadRequest`
    :return: :class:`HttpResponseRedirect` object
    """
    course_id = int(course_id)
    user = request.user
    user_credentials = (user.username, user.password)
    # Check if a user is not an organizer as he can't attend his own course
    course = api.get_course(course_id, auth=user_credentials)
    organizer = course.courseOrganizer
    is_organizer = user_is_organizer(user, organizer)
    if not is_organizer:
        api.attend_course(course_id, auth=user_credentials)
        return redirect(reverse(course_page, args=[course_id]))
    else:
        return HttpResponseBadRequest()


@require_GET
@login_required(login_url='/accounts/login/')
def attendee_solutions(request, course_id, attendee_id):
    """
    Attendee solutions view. Gets a list of attendee solutions, and generates
    `courses/attendee_solutions.html` template as a response.

    :param request: :class:`Request` object
    :param course_id: Id of the course to add new user at
    :type course_id: int
    :param attendee_id: Id of the attendee to get solutions of
    :type attendee_id: int
    :return: :class:`HttpResponse` object
    """
    course_id = int(course_id)
    attendee_id = int(attendee_id)
    user_credentials = (request.user.username, request.user.password)
    solutions = api.get_attendee_solutions(course_id, attendee_id, auth=user_credentials)
    params = {}
    if solutions:
        attendee = solutions[0].attendee.user
        attendee_img_url = api.get_user_avatar_url(attendee.id)
        solutions_per_assignment = defaultdict(list)
        for item in solutions:
            assignment = item.assignment
            solution = clean_solution(item)
            solutions_per_assignment[assignment].append(solution)
        params = {'attendee': attendee,
                  'attendee_img_url': attendee_img_url,
                  'solutions_per_assignment': dict(solutions_per_assignment)}
    return render(request, 'courses/attendee_solutions.html', params)


@login_required(login_url='/accounts/login/')
def delete_course(request, course_id):
    """
    Delete course view. Requests an API to delete a course.

    :param request: :class:`Request` object
    :param course_id: Id of the course to delete
    :return: :class:`HttpResponseRedirect` object
    """
    course_id = int(course_id)
    user_credentials = (request.user.username, request.user.password)
    api.delete_course(course_id, auth=user_credentials)
    return redirect(reverse(course_list))