from .utils import process_request
from ..users.models import UserProfile


def get_courses(**kwargs):
    url = '/courses/'
    response = process_request('GET', url)
    return response.course


def get_course(course_id):
    url = '/course/{}'.format(course_id)


def get_assignments(course_id):
    url = '/courses/{}/assignments/'.format(course_id)


def get_assignment(course_id, assignment_id):
    url = '/courses/{}/assignments/{}'.format(course_id, assignment_id)


def get_solutions(course_id, assignment_id):
    url = '/courses/{}/assignments/{}/solutions/'.format(course_id, assignment_id)


def get_attendee_solutions(course_id, attendee_id, auth):
    url = '/courses/{}/solutions?attendeeId={}'.format(course_id, attendee_id)
    response = process_request('GET', url, auth=auth)
    return response.solution


def get_user_avatar_url(user_id):
    user = UserProfile.objects.get(user__id=user_id)
    avatar = user.avatar
    return avatar.url


def create_course():
    url = '/courses/'


def create_assignment(course_id):
    url = '/courses/{}/assignments/'


def create_solution(course_id, assignment_id):
    url = '/courses/{}/assignments/{}/solutions/'.format(course_id, assignment_id)


def create_attendee(course_id):
    url = '/courses/{}/attendees/'.format(course_id)


def update_course():
    pass


def delete_course(course_id):
    url = '/courses/{}'.format(course_id)


def delete_assignment():
    pass


def delete_solution():
    pass