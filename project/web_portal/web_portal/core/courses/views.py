import json
import requests
import urlparse
from collections import namedtuple, defaultdict

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404, HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST, require_GET

import api
from .forms import CourseForm, AssignmentForm, SolutionForm, LANGUAGES
from .utils import clean_solution
from ..users.models import UserProfile

POST_JSON_HEADER = {'content-type': 'application/json'}
GET_JSON_HEADER = {'accept': 'application/json'}


def get_page_and_params(request, key='page'):
    p = urlparse.parse_qsl(request.META['QUERY_STRING'])
    dic = dict(p)
    page = dic.pop(key, 1)
    return page, dic


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


@require_GET
def course_list(request):
    page, dic = get_page_and_params(request)
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
def attendee_solutions(request, course_id, attendee_id):
    course_id = int(course_id)
    attendee_id = int(attendee_id)
    user_credentials = (request.user.username, request.user.password)
    solutions = api.get_attendee_solutions(course_id, attendee_id, user_credentials)
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


@require_POST
@login_required(login_url='/accounts/login/')
def add_course(request):
    form = CourseForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        params = {'name': name, 'description': description}
        r = requests.post(settings.REST_API+'/courses/', data=json.dumps(params), headers=POST_JSON_HEADER,
                          auth=(request.user.username, request.user.password))
        if r.status_code == requests.codes.created:
            location = r.headers['location']
            new_course_id = location.split('/')[-1]
            return HttpResponse(
                json.dumps({'url': '/courses/{0}/'.format(new_course_id)}),
                content_type="application/json")
    raise Http404()


def course_page(request, pk):
    try:
        pk = int(pk)
    except ValueError:
        raise Http404()
    r = requests.get(settings.REST_API+'/courses/{0}'.format(pk), headers=GET_JSON_HEADER)
    if r.status_code != requests.codes.ok:
        raise Http404()
    course = r.json(object_hook=_json_object_hook)
    user = request.user
    attendees = course.courseAttendees
    attendees_id = [attendee.user.id for attendee in attendees]
    attendees = [attendee.user for attendee in attendees]
    if user.is_authenticated() and user.is_active and course.courseOrganizer.id == user.id:
        organizer = user
    else:
        organizer = None
    not_attendee = False
    if not organizer and (user.id not in attendees_id or not user.is_authenticated()):
        not_attendee = True
    assignments = None
    if not not_attendee or organizer:
        r = requests.get(settings.REST_API+'/courses/{0}/assignments/'.format(pk), headers=GET_JSON_HEADER,
                         auth=(user.username, user.password))
        json_resp = r.json(object_hook=_json_object_hook)
        assignments = json_resp.assignment
    avatar = UserProfile.objects.get(user__id=course.courseOrganizer.id).avatar
    organizer_img = avatar.url
    return render(request, 'courses/course_page.html',
                  {'course': course,
                   'assignments': assignments,
                   'organizer': organizer,
                   'not_attendee': not_attendee,
                   'attendees': attendees,
                   'organizer_img': organizer_img,
                   'languages': [[l[0], l[1]] for l in LANGUAGES]})


@login_required(login_url='/accounts/login/')
def edit_course(request, pk):
    try:
        pk = int(pk)
    except ValueError:
        raise Http404()
    r = requests.get(settings.REST_API+'/courses/{0}'.format(pk), headers=GET_JSON_HEADER)
    if r.status_code != requests.codes.ok:
        raise Http404()
    course = r.json(object_hook=_json_object_hook)
    user = request.user
    if course.courseOrganizer.id != user.id:
        raise Http404()
    data = {'name': course.name, 'description': course.description}
    form = CourseForm(data)
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            params = {'name': name, 'description': description}
            r = requests.put(settings.REST_API+'/courses/{0}'.format(pk), data=json.dumps(params), headers=POST_JSON_HEADER,
                              auth=(user.username, user.password))
            if r.status_code == requests.codes.no_content:
                return redirect('/courses/{0}/'.format(pk))
            else:
                raise Http404()
    return render(request, 'courses/add_course.html',
                  {'form': form, 'edit': True})


@login_required(login_url='/accounts/login/')
def delete_course(request, pk):
    try:
        pk = int(pk)
    except ValueError:
        raise Http404()
    r = requests.get(settings.REST_API+'/courses/{0}'.format(pk), headers=GET_JSON_HEADER)
    if r.status_code == requests.codes.ok:
        course = r.json(object_hook=_json_object_hook)
        user = request.user
        if course.courseOrganizer.id == user.id:
            r = requests.delete(settings.REST_API+'/courses/{0}/'.format(pk), auth=(user.username, user.password))
            if r.status_code == requests.codes.no_content:
                return redirect('/courses/')
    raise Http404()


@require_POST
@login_required(login_url='/accounts/login/')
def add_assignment(request, pk):
    pk = int(pk)  # course id
    if request.is_ajax():
        form = AssignmentForm(request.POST)
        if form.is_valid():
            params = {'name': form.cleaned_data['name'],
                      'description': form.cleaned_data['description'],
                      'language': form.cleaned_data['language'],
                      'templateCode': form.cleaned_data['template_code'],
                      'verificationCode': form.cleaned_data['verification_code'],
                      }
            r = requests.post(settings.REST_API+'/courses/{0}/assignments'.format(pk),
                              data=json.dumps(params),
                              headers=POST_JSON_HEADER,
                              auth=(request.user.username, request.user.password))
            if r.status_code == requests.codes.created:
                location = r.headers['location']
                url = location.replace(settings.SERVER_URL, '')
                return HttpResponse(json.dumps({'url': url}),
                                    content_type="application/json")
    raise Http404()


@login_required(login_url='/accounts/login/')
def assignment_page(request, pk, apk):
    # TODO add organizer check if editing of assignment is necessary
    pk = int(pk)  # course id
    apk = int(apk)  # assignment id

    url = '{0}/courses/{1}/assignments/'.format(settings.REST_API, pk, apk)
    r = requests.get(url,
                     headers=GET_JSON_HEADER,
                     auth=(request.user.username, request.user.password))
    if r.status_code != requests.codes.ok:
        if r.status_code == requests.codes.forbidden:
            raise PermissionDenied
        else:
            raise Http404()
    response = r.json(object_hook=_json_object_hook)
    assignments = response.assignment
    for item in assignments:
        if item.id == apk:
            assignment = item
            break
    else:
        raise PermissionDenied
    if response.course.courseOrganizer.id == request.user.id:
        organizer = True
    else:
        organizer = False
    if not organizer:
        url = '{0}/courses/{1}/assignments/{2}/solutions/'.format(settings.REST_API, pk, apk)
        r = requests.get(url,
                         headers=GET_JSON_HEADER,
                         auth=(request.user.username, request.user.password))
        if r.status_code != requests.codes.ok:
            if r.status_code == requests.codes.forbidden:
                raise PermissionDenied
            else:
                raise Http404()
        response = r.json(object_hook=_json_object_hook)
        solutions = response.solution
    else:
        solutions = None

    return render(request, 'courses/assignment_page.html', {
        'assignments': assignments,
        'assignment': assignment,
        'solutions': solutions,
        'organizer': organizer,
        'course_id': pk})


@login_required(login_url='/accounts/login/')
def delete_assignment(request, pk, apk):
    try:
        #course id
        pk = int(pk)
        #assignment id
        apk = int(apk)
    except ValueError:
        raise Http404()
    r = requests.get(settings.REST_API+'/courses/{0}/assignments/{1}'.format(pk, apk), headers=GET_JSON_HEADER,
                     auth=(request.user.username, request.user.password))
    if r.status_code != requests.codes.ok:
        raise Http404()
    user = request.user
    r = requests.delete(settings.REST_API+'/courses/{0}/assignments/{1}'.format(pk, apk),
                        auth=(user.username, user.password))
    if r.status_code == requests.codes.no_content:
        return redirect('/courses/{0}/'.format(pk))
    raise Http404()


@login_required(login_url='/accounts/login/')
def attend_course(request, pk):
    try:
        #course id
        pk = int(pk)
    except ValueError:
        raise Http404()
    r = requests.post(settings.REST_API+'/courses/{0}/attendees'.format(pk), headers=POST_JSON_HEADER,
                              auth=(request.user.username, request.user.password))
    if r.status_code == requests.codes.created:
        return redirect('/courses/{0}/'.format(pk))
    else:
        raise Http404()


@require_POST
@login_required(login_url='/accounts/login/')
def add_solution(request, pk, apk):
    pk = int(pk)  # course id
    apk = int(apk)  # assignment id
    if request.is_ajax():
        form = SolutionForm(request.POST)
        if form.is_valid():
            params = {'code': form.cleaned_data['code']}
            r = requests.post(settings.REST_API+'/courses/{0}/assignments/{1}/solutions'.format(pk, apk),
                              data=json.dumps(params), headers=POST_JSON_HEADER,
                              auth=(request.user.username, request.user.password))
            if r.status_code == requests.codes.created:
                location = r.headers['location']
                new_solution_id = location.split('/')[-1]
                url = '/courses/{0}/assignments/{1}/solutions/{2}'.format(
                    pk, apk, new_solution_id)
                return HttpResponse(json.dumps({'url': url}),
                                    content_type="application/json")
    raise Http404()


@login_required(login_url='/accounts/login/')
def solution_page(request, pk, apk, spk):
    pk = int(pk)  # course id
    apk = int(apk)  # assignment id
    spk = int(spk)  # solution id
    url = '{0}/courses/{1}/assignments/'.format(settings.REST_API, pk, apk)
    r = requests.get(url,
                     headers=GET_JSON_HEADER,
                     auth=(request.user.username, request.user.password))
    if r.status_code != requests.codes.ok:
        if r.status_code == requests.codes.forbidden:
            raise PermissionDenied
        else:
            raise Http404()
    response = r.json(object_hook=_json_object_hook)
    assignments = response.assignment
    for item in assignments:
        if item.id == apk:
            assignment = item
    url = settings.REST_API+'/courses/{0}/assignments/{1}/solutions/'.format(pk, apk)
    r = requests.get(url, headers=GET_JSON_HEADER,
                     auth=(request.user.username, request.user.password))
    if r.status_code != requests.codes.ok:
        if r.status_code == requests.codes.forbidden:
            raise PermissionDenied
        else:
            raise Http404()
    response = r.json(object_hook=_json_object_hook)
    solutions = response.solution
    for item in solutions:
        if item.id == spk:
            solution = item
            break
    else:
        raise PermissionDenied
    return render(request, 'courses/solution_page.html',
                  {'assignments': assignments, 'assignment': assignment,
                   'curr_solution': solution, 'solutions': solutions,
                   'course_id': pk})


@login_required(login_url='/accounts/login/')
def delete_solution(request, pk, apk, spk):
    try:
        #course id
        pk = int(pk)
        #assignment id
        apk = int(apk)
        #solution id
        spk = int(spk)
    except ValueError:
        raise Http404()
    user = request.user
    r = requests.delete(settings.REST_API+'/courses/{0}/assignments/{1}/solutions/{2}'.format(pk, apk, spk),
                        auth=(user.username, user.password))
    if r.status_code == requests.codes.no_content:
        return redirect('/courses/{0}/asignment/{1}/'.format(pk, apk))
    raise Http404()