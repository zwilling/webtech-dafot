from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from forms import CourseForm, CourseSearchForm, AssignmentForm, SolutionForm
from django.http import Http404
from django.shortcuts import redirect, render
import requests
import urlparse
import json
from collections import namedtuple
from web_portal.settings import SERVER_URL
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import connection

def get_page_and_params(request, key = 'page'):
    p = urlparse.parse_qsl(request.META['QUERY_STRING'])
    dic = dict(p)
    if dic.has_key(key):
        page = dic[key]
        del dic[key]
    else:
        page = 1
    return (page, dic)

def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())

def course_list(request):
    page, dic = get_page_and_params(request)
    if request.method == "GET":
        form = CourseSearchForm()
        r = requests.get(SERVER_URL+'/courses/', headers=GET_JSON_HEADER)
    if request.method == "POST":
        form = CourseSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            params = {'name': name}
            r = requests.get(SERVER_URL+'/courses/', params=params, headers=GET_JSON_HEADER)
        else:
            return render(request, 'courses/course_list.html',
                          {'form': form, })
    json_resp = r.json(object_hook=_json_object_hook)
    courses = json_resp.course
    paginator = None
    if request.method == "GET":
        paginator = Paginator(courses, 5)
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
            description = form.cleaned_data['description']
            params = {'name': name, 'description': description}
            r = requests.post(SERVER_URL+'/courses/', data=json.dumps(params), headers=POST_JSON_HEADER,
                              auth=(request.user.username, request.user.password))
            print(r.request.__dict__)
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
    r = requests.get(SERVER_URL+'/courses/{0}'.format(pk), headers=GET_JSON_HEADER)
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
    if user.is_authenticated() and user.is_active:
        r = requests.get(SERVER_URL+'/courses/{0}/assignments/'.format(pk), headers=GET_JSON_HEADER,
                         auth=(user.username, user.password))
        json_resp = r.json(object_hook=_json_object_hook)
        assignments = json_resp.assignment
    return render(request, 'courses/course_page.html',
                  {'course': course, 'assignments': assignments, 'organizer': organizer,
                   'not_attendee': not_attendee, 'attendees': attendees})

@login_required(login_url='/accounts/login/')
def edit_course(request, id):
    #TODO
    pass

@login_required(login_url='/accounts/login/')
def delete_course(request, pk):
    try:
        pk = int(pk)
    except ValueError:
        raise Http404()
    r = requests.get(SERVER_URL+'/courses/{0}'.format(pk), headers=GET_JSON_HEADER)
    if r.status_code == requests.codes.ok:
        course = r.json(object_hook=_json_object_hook)
        user = request.user
        if course.courseOrganizer.id == user.id:
            r = requests.delete(SERVER_URL+'/courses/{0}/'.format(pk), auth=(user.username, user.password))
            if r.status_code == requests.codes.no_content:
                return redirect('/courses/')
    raise Http404()

@login_required(login_url='/accounts/login/')
def add_assignment(request, pk):
    try:
        #course id
        pk = int(pk)
    except ValueError:
        raise Http404()
    user = request.user
    form = AssignmentForm()
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            template_code = form.cleaned_data['template_code']
            verification_code = form.cleaned_data['verification_code']
            language = form.cleaned_data['language']
            params = {'name': name, 'description': description, 'templateCode': template_code,
                      'verificationCode': verification_code, 'language': language}
            r = requests.post(SERVER_URL+'/courses/{0}/assignments'.format(pk),
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
    try:
        #course id
        pk = int(pk)
        #assignment id
        apk = int(apk)
    except ValueError:
        raise Http404()
    r = requests.get(SERVER_URL+'/courses/{0}'.format(pk), headers=GET_JSON_HEADER)
    if r.status_code != requests.codes.ok:
        raise Http404()
    course = r.json(object_hook=_json_object_hook)
    user = request.user
    attendees = course.courseAttendees
    attendees_id = [attendee.user.id for attendee in attendees]
    attendees = [attendee.user for attendee in attendees]
    if course.courseOrganizer.id == user.id:
        organizer = user
    else:
        organizer = None
    attendee = None
    solutions = None
    if not organizer and (user.id in attendees_id):
        attendee = request.user
        r = requests.get(SERVER_URL+'/courses/{0}/assignments/{1}/solutions/'.format(pk, apk), headers=GET_JSON_HEADER,
                         auth=(user.username, user.password))
        json_resp = r.json(object_hook=_json_object_hook)
        solutions = json_resp.solution
    r = requests.get(SERVER_URL+'/courses/{0}/assignments/{1}'.format(pk, apk), headers=GET_JSON_HEADER,
                     auth=(request.user.username, request.user.password))
    if r.status_code != requests.codes.ok:
        raise Http404()
    assignment = r.json(object_hook=_json_object_hook)
    return render(request, 'courses/assignment_page.html',
                  {'assignment': assignment, 'course': course, 'organizer': organizer,
                   'attendee': attendee, 'solutions': solutions})

@login_required(login_url='/accounts/login/')
def delete_assignment(request, pk, apk):
    try:
        #course id
        pk = int(pk)
        #assignment id
        apk = int(apk)
    except ValueError:
        raise Http404()
    r = requests.get(SERVER_URL+'/courses/{0}/assignments/{1}'.format(pk, apk), headers=GET_JSON_HEADER,
                     auth=(request.user.username, request.user.password))
    if r.status_code != requests.codes.ok:
        raise Http404()
    user = request.user
    r = requests.delete(SERVER_URL+'/courses/{0}/assignments/{1}'.format(pk, apk),
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
    #TODO: change this
    cursor = connection.cursor()
    sql = 'insert into attendee(course_id, user_id) values ({0}, {1})'.format(pk, request.user.id)
    cursor.execute(sql)
    return redirect('/courses/{0}/'.format(pk))

@login_required(login_url='/accounts/login/')
def attendee_page(request, pk, apk):
    try:
        #course id
        pk = int(pk)
        #attendee id
        apk = int(apk)
    except ValueError:
        raise Http404()
    #TODO: change this
    return redirect('/courses/{0}/'.format(pk))

@login_required(login_url='/accounts/login/')
def add_solution(request, pk, apk):
    try:
        #course id
        pk = int(pk)
        #assignment id
        apk = int(apk)
    except ValueError:
        raise Http404()
    r = requests.get(SERVER_URL+'/courses/{0}'.format(pk), headers=GET_JSON_HEADER)
    if r.status_code != requests.codes.ok:
        raise Http404()
    course = r.json(object_hook=_json_object_hook)
    user = request.user
    attendees = course.courseAttendees
    attendees_id = [attendee.user.id for attendee in attendees]
    if course.courseOrganizer.id == user.id or (user.id not in attendees_id):
        raise Http404()

    form = SolutionForm
    if request.method == 'POST':
        if request.POST.has_key('cancel'):
            return redirect('/courses/{0}/assignments/{1}/'.format(pk, apk))
        form = SolutionForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            params = {'code': code}
            r = requests.post(SERVER_URL+'/courses/{0}/assignments/{1}/solutions'.format(pk, apk),
                              data=json.dumps(params), headers=POST_JSON_HEADER,
                              auth=(user.username, user.password))
            if r.status_code == requests.codes.created:
                location = r.headers['location']
                new_solution_id = location.split('/')[-1]
                return redirect('/courses/{0}/assignments/{1}/'.format(pk, apk))
            else:
                raise Http404()
    return render(request, 'main/form.html',
                      {'form': form, 'title': 'Add Solution'})

@login_required(login_url='/accounts/login/')
def solution_page(request, pk, apk, spk):
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
    r = requests.get(SERVER_URL+'/courses/{0}/assignments/{1}/solutions/{2}'.format(pk, apk, spk),
                     headers=GET_JSON_HEADER, auth=(user.username, user.password))
    if r.status_code != requests.codes.ok:
        raise Http404()
    solution = r.json(object_hook=_json_object_hook)
    return render(request, 'courses/solution_page.html',
                  {'solution': solution, 'course_id': pk})


POST_JSON_HEADER = {'content-type': 'application/json'}
GET_JSON_HEADER = {'accept': 'application/json'}