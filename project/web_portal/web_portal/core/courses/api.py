from .utils import process_request
from ..users.models import UserProfile


def get_courses(**kwargs):
    """
    Gets a list of all courses by sending a GET request.

    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: Json-encoded content of a response, if any.
    """
    url = '/courses/'
    response = process_request('GET', url, **kwargs)
    return response.course


def get_course(course_id, **kwargs):
    """
    Gets a course by id by sending a GET request.

    :param course_id: Id of the course
    :type course_id: int
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: Json-encoded content of a response, if any.
    """
    url = '/courses/{}/'.format(course_id)
    response = process_request('GET', url, **kwargs)
    return response


def get_assignments(course_id, clipped_body=True, **kwargs):
    """
    Gets a list of all assignments of the course by sending a GET request.

    :param course_id: Id of the course
    :type course_id: int
    :param clipped_body: Return a full response if set to True, otherwise \
    return only `assignment` attribute of a response.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: Json-encoded content of a response, if any.
    """
    url = '/courses/{}/assignments/'.format(course_id)
    response = process_request('GET', url, **kwargs)
    return response.assignment if clipped_body else response


def get_assignment(course_id, assignment_id, **kwargs):
    """
    Gets an assignment of the course by id by sending a GET request.

    :param course_id: Id of the course
    :type course_id: int
    :param assignment_id: Id of the assignment
    :type assignment_id: int
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: Json-encoded content of a response, if any.
    """
    url = '/courses/{}/assignments/{}'.format(course_id, assignment_id)
    response = process_request('GET', url, **kwargs)
    return response


def get_solutions(course_id, assignment_id, **kwargs):
    """
    Gets a list of all solutions of an assignment in the course by sending a
    GET request.

    :param course_id: Id of the course
    :type course_id: int
    :param assignment_id: Id of the assignment
    :type assignment_id: int
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: Json-encoded content of a response, if any.
    """
    url = '/courses/{}/assignments/{}/solutions/'.format(course_id, assignment_id)
    response = process_request('GET', url, **kwargs)
    return response.solution


def get_attendee_solutions(course_id, attendee_id, **kwargs):
    """
    Gets a list of all solutions of an attendee in the course by sending a
    GET request.

    :param course_id: Id of the course
    :type course_id: int
    :param attendee_id: Id of the attendee of the course
    :type attendee_id: int
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: Json-encoded content of a response, if any.
    """
    url = '/courses/{}/solutions?attendeeId={}'.format(course_id, attendee_id)
    response = process_request('GET', url, **kwargs)
    return response.solution


def get_user_avatar_url(user_id):
    """
    Gets an url of the avatar of the user.

    :param user_id: Id of the user
    :type user_id: int
    :returns: Url to user's avatar
    """
    user = UserProfile.objects.get(user__id=user_id)
    avatar = user.avatar
    return avatar.url


def create_course(json_data, **kwargs):
    """
    Creates a new course by sending a POST request.

    :param json_data: Course json representation
    :type json_data: dict
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: Url of the created course
    """
    url = '/courses/'
    response = process_request('POST', url, json=json_data, return_only_body=False, **kwargs)
    return response.headers['location']


def create_assignment(course_id, json_data, **kwargs):
    """
    Creates a new assignment by sending a POST request.

    :param course_id: Id of the course to create new assignment in
    :type course_id: int
    :param json_data: Assignment json representation
    :type json_data: dict
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: Url of the created assignment
    """
    url = '/courses/{}/assignments/'.format(course_id)
    response = process_request('POST', url, json=json_data, return_only_body=False, **kwargs)
    return response.headers['location']


def create_solution(course_id, assignment_id, json_data, **kwargs):
    """
    Creates a new solution by sending a POST request.

    :param course_id: Id of the course to create new solution in
    :type course_id: int
    :param assignment_id: Id of the assignment to create new solution in
    :type assignment_id: int
    :param json_data: Solution json representation
    :type json_data: dict
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: Url of the created solution
    """
    url = '/courses/{}/assignments/{}/solutions/'.format(course_id, assignment_id)
    response = process_request('POST', url, json=json_data, return_only_body=False, **kwargs)
    return response.headers['location']


def attend_course(course_id, **kwargs):
    """
    Adds a user to the course by sending a POST request..

    :param course_id: Id of the course to create new solution in
    :type course_id: int
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: Url of the added attendee
    """
    url = '/courses/{}/attendees/'.format(course_id)
    response = process_request('POST', url, return_only_body=False, **kwargs)
    return response.headers['location']


def delete_course(course_id, **kwargs):
    """
    Deletes a course by sending a DELETE request.

    :param course_id: Id of the course to create new solution in
    :type course_id: int
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: Json-encoded content of a response, if any.
    """
    url = '/courses/{}'.format(course_id)
    response = process_request('DELETE', url, return_json=False, **kwargs)
    return response