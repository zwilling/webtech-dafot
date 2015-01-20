import requests
from collections import namedtuple
from functools import wraps

from django.conf import settings


def base_request_url(path):
    """Decorator for API that adds server address to the url beginning."""
    def func_wrapper(func):
        @wraps(func)
        def returned_wrapper(url, *args, **kwargs):
            url = path + url
            return func(url, *args, **kwargs)
        return returned_wrapper
    return func_wrapper


def json_object_hook(response):
    """Convert JSON representation of response to object one."""
    return namedtuple('JSONResponse', response.keys())(*response.values())


def user_is_attendee(user, attendees):
    """Check whether current user is in the attendees list."""
    return any(user.id == attendee.id for attendee in attendees)


def user_is_organizer(user, organizer):
    """Check whether current user is organizer of the course."""
    return user.id == organizer.id


def clean_solution(solution):
    """Remove `assignment` and `attendee` attributes from solution

    :param: solution: Solution object of :type:`namedtuple`
    """
    clean_fields = ['assignment', 'attendee']
    dictionary = solution._asdict()
    for field in clean_fields:
        dictionary.pop(field, None)
    return namedtuple('Solution', dictionary.keys())(**dictionary)


def process_request(method, url, data=None, return_json=True, **kwargs):
    """Process request by send it, check its status and return response.

    :param method: Method of the ``request``.
    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, bytes, or file-like object to send in
    the body of the POST :class:`Request`.
    :param return_json: Return the response as :class:`Response` object or
    JSON-view object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    """
    if method == 'GET':
        response = send_get_request(url, **kwargs)
    elif method == 'POST':
        response = send_post_request(url, data, **kwargs)
    elif method == 'DELETE':
        response = send_delete_request(url, **kwargs)
    else:
        raise ValueError('Method {} not allowed.'.format(method))
    response.raise_for_status()
    if return_json:
        return response.json(object_hook=json_object_hook)
    else:
        return response


@base_request_url(settings.REST_API)
def send_get_request(url, headers=None, **kwargs):
    """Sends a GET request. Returns :class:`Response` object.

    :param url: URL for the new :class:`Request` object.
    :param headers: Headers used for the new :class: `Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    """
    accept_json_header = {'accept': 'application/json'}
    headers = prepare_headers(headers, accept_json_header)
    return requests.get(url, headers=headers, **kwargs)


@base_request_url(settings.REST_API)
def send_post_request(url, headers=None, data=None, **kwargs):
    """Sends a POST request. Returns :class:`Response` object.

    :param url: URL for the new :class:`Request` object.
    :param headers: Headers used for the new :class: `Request` object.
    :param data: (optional) Dictionary, bytes, or file-like object to send in
    the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    """
    json_content_type_header = {'content-type': 'application/json'}
    headers = prepare_headers(headers, json_content_type_header)
    return requests.post(url, headers=headers, data=data, **kwargs)


@base_request_url(settings.REST_API)
def send_delete_request(url, **kwargs):
    """Sends a DELETE request. Returns :class:`Response` object.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    """
    return requests.delete(url, **kwargs)


def prepare_headers(current_headers, obligatory_headers):
    """Adds :param: `obligatory_headers` to :param: `current_headers` if they
    not already included.

    :param: current_headers: Dict of original headers
    :param: obligatory_headers: Dict of obligatory headers, which should be
    added
    """
    if current_headers is None:
        headers = obligatory_headers
    else:
        for key, value in obligatory_headers.iteritems():
            if key not in current_headers:
                current_headers.update({key: value})
        headers = current_headers
    return headers