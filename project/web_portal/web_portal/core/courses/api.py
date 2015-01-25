from .utils import process_request
from ..users.models import UserProfile


def get_courses(**kwargs):
    url = '/courses/'
    response = process_request('GET', url, **kwargs)
    return response.course


def get_course(course_id, **kwargs):
    url = '/courses/{}/'.format(course_id)
    response = process_request('GET', url, **kwargs)
    return response


def get_assignments(course_id, clipped_body=True, **kwargs):
    url = '/courses/{}/assignments/'.format(course_id)
    response = process_request('GET', url, **kwargs)
    return response.assignment if clipped_body else response


def get_assignment(course_id, assignment_id, **kwargs):
    url = '/courses/{}/assignments/{}'.format(course_id, assignment_id)
    response = process_request('GET', url, **kwargs)
    return response


def get_solutions(course_id, assignment_id, **kwargs):
    url = '/courses/{}/assignments/{}/solutions/'.format(course_id, assignment_id)
    response = process_request('GET', url, **kwargs)
    return response.solution


def get_attendee_solutions(course_id, attendee_id, **kwargs):
    url = '/courses/{}/solutions?attendeeId={}'.format(course_id, attendee_id)
    response = process_request('GET', url, **kwargs)
    return response.solution


def get_user_avatar_url(user_id):
    user = UserProfile.objects.get(user__id=user_id)
    avatar = user.avatar
    return avatar.url


def create_course(json_data, **kwargs):
    url = '/courses/'
    response = process_request('POST', url, json=json_data, return_only_body=False, **kwargs)
    return response.headers['location']


def create_assignment(course_id, json_data, **kwargs):
    url = '/courses/{}/assignments/'.format(course_id)
    response = process_request('POST', url, json=json_data, return_only_body=False, **kwargs)
    return response.headers['location']


def create_solution(course_id, assignment_id, json_data, **kwargs):
    url = '/courses/{}/assignments/{}/solutions/'.format(course_id, assignment_id)
    response = process_request('POST', url, json=json_data, return_only_body=False, **kwargs)
    return response.headers['location']


def attend_course(course_id, **kwargs):
    url = '/courses/{}/attendees/'.format(course_id)
    response = process_request('POST', url, return_only_body=False, **kwargs)
    return response.headers['location']


def update_course():
    pass


def delete_course(course_id, **kwargs):
    url = '/courses/{}'.format(course_id)
    response = process_request('DELETE', url, return_json=False, **kwargs)
    return response