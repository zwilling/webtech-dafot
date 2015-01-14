import json
import requests
import urlparse
from collections import namedtuple

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404, HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import CourseForm, CourseSearchForm, AssignmentForm, SolutionForm
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


def course_list(request):
    page, dic = get_page_and_params(request)
    if request.method == "GET":
        form = CourseSearchForm()
        r = requests.get(settings.REST_API+'/courses/', headers=GET_JSON_HEADER)
    if request.method == "POST":
        form = CourseSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            params = {'name': name}
            r = requests.get(settings.REST_API+'/courses/', params=params, headers=GET_JSON_HEADER)
        else:
            return render(request, 'courses/course_list.html',
                          {'form': form, })
    json_resp = r.json(object_hook=_json_object_hook)
    courses = json_resp.course
    paginator = None
    if request.method == "GET":
        paginator = Paginator(courses, 4)
        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
            courses = paginator.page(1)
        except EmptyPage:
            courses = paginator.page(paginator.num_pages)
    return render(request, 'courses/course_list.html',
                  {'courses': courses, 'form': form, 'paginator': paginator})


@login_required(login_url='/accounts/login/')
def add_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = '<![CDATA[{}]]>'.format(form.cleaned_data['description'])
            params = {'name': name, 'description': description}
            r = requests.post(settings.REST_API+'/courses/', data=json.dumps(params), headers=POST_JSON_HEADER,
                              auth=(request.user.username, request.user.password))
            if r.status_code == requests.codes.created:
                location = r.headers['location']
                new_course_id = location.split('/')[-1]
                return redirect('/courses/{0}/'.format(new_course_id))
            else:
                raise Http404()
    return render(request, 'courses/add_course.html',
                  {'form': form, 'edit': False})


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
                  {'course': course, 'assignments': assignments, 'organizer': organizer,
                   'not_attendee': not_attendee, 'attendees': attendees,
                   'organizer_img': organizer_img})


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


@login_required(login_url='/accounts/login/')
def add_assignment(request, pk):
    pk = int(pk)  # course id
    user = request.user
    form = AssignmentForm()
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = '<![CDATA[{}]]>'.format(form.cleaned_data['description'])
            template_code = form.cleaned_data['template_code']
            verification_code = form.cleaned_data['verification_code']
            language = form.cleaned_data['language']
            params = {'name': name, 'description': description, 'templateCode': template_code,
                      'verificationCode': verification_code, 'language': language}
            r = requests.post(settings.REST_API+'/courses/{0}/assignments'.format(pk),
                              data=json.dumps(params), headers=POST_JSON_HEADER,
                              auth=(user.username, user.password))
            print(r.request.__dict__)
            if r.status_code == requests.codes.created:
                location = r.headers['location']
                new_assignment_id = location.split('/')[-1]
                return redirect('/courses/{0}/'.format(pk))
            else:
                raise Http404()
    return render(request, 'courses/add_assignment.html',
                      {'form': form, 'course_id': pk,'edit': False})


@login_required(login_url='/accounts/login/')
def assignment_page(request, pk, apk):
    # TODO add organizer check if editing of assignment is necessary
    pk = int(pk)  # course id
    apk = int(apk)  # assignment id
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
    return render(request, 'courses/assignment_page.html', {
        'assignments': assignments, 'assignment': assignment,
        'solutions': solutions, 'course_id': pk})


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


@login_required(login_url='/accounts/login/')
def attendee_solutions(request, pk, apk):
    try:
        #course id
        pk = int(pk)
        #attendee id
        apk = int(apk)
    except ValueError:
        raise Http404()
    #TODO: change this
    return render(request, 'main/coming.html')


@require_POST
@login_required(login_url='/accounts/login/')
def add_solution(request, pk, apk):
    try:
        pk = int(pk)  # course id
        apk = int(apk)  # assignment id
    except ValueError:
        raise Http404()
    if request.method == 'POST' and request.is_ajax():
        form = SolutionForm(request.POST)
        if form.is_valid():
            params = {'code': form.cleaned_data['code']}
            r = requests.post(settings.REST_API+'/courses/{0}/assignments/{1}/solutions'.format(pk, apk),
                              data=json.dumps(params), headers=POST_JSON_HEADER,
                              auth=(request.user.username, request.user.password))
            if r.status_code == requests.codes.created:
                location = r.headers['location']
                return HttpResponse(json.dumps({'url': location}),
                                    content_type="application/json")
            else:
                raise Http404()
    else:
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