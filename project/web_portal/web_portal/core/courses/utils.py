import requests
import urlparse
from collections import namedtuple
from functools import wraps

from django.conf import settings


def base_request_url(path):
    """
    Decorator for API that adds server address to the url beginning.

    :param path: url
    :type path: str
    """
    def func_wrapper(func):
        @wraps(func)
        def returned_wrapper(url, *args, **kwargs):
            url += path
            return func(url, *args, **kwargs)
        return returned_wrapper
    return func_wrapper


def json_object_hook(response):
    """
    Convert JSON representation of response to object one.

    :param response: :class:`HTTPResponse` object
    :returns: :class:`JSONResponse` object
    """
    return namedtuple('JSONResponse', response.keys())(*response.values())


def get_page_from_request(request, key='page'):
    """
    Get current page number from the request

    :param request: :class:`Request` object
    :param key: Optional key to extract from the query string instead of page
    :type key: str
    :returns: Page number
    """
    params = dict(urlparse.parse_qsl(request.META['QUERY_STRING']))
    page = params.pop(key, 1)
    return page


def user_is_attendee(user, attendees):
    """
    Check whether current user is in the attendees list.

    :param user: :class:`User` object
    :param attendees: a list of :class:`User` objects, who are attendees of the course
    :returns: `True` if a user is attendee, `False` otherwise
    """
    return any(user.id == attendee.user.id for attendee in attendees)


def user_is_organizer(user, organizer):
    """
    Check whether current user is organizer of the course.

    :param user: :class:`User` object
    :param organizer: :class:`User` object representing organizer of the course
    :returns: `True` if a user is organizer, `False` otherwise
    """
    return user.id == organizer.id


def clean_solution(solution):
    """
    Remove `assignment` and `attendee` attributes from solution

    :param: solution: :class:`Solution` object
    :returns: :class:`Solution` object
    """
    clean_fields = ['assignment', 'attendee']
    dictionary = solution._asdict()
    for field in clean_fields:
        dictionary.pop(field, None)
    return namedtuple('Solution', dictionary.keys())(**dictionary)


def clean_location(location):
    """
    Remove REST API address from location

    :param: location: Url address
    :returns: url without REST API
    """
    return location.replace(settings.REST_API, '')


def process_request(method, url, data=None, return_only_body=True, **kwargs):
    """Process request by send it, check its status and return response.

    :param method: Method of the ``request``.
    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the POST :class:`Request`.
    :param return_only_body: Return only message-body of the response as JSON-view object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: :class:`HTTPResponse` object if `return_only_body` set to `False`,else :class:`JSONResponse` object
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
    if return_only_body:
        return response.json(object_hook=json_object_hook)
    else:
        return response


@base_request_url(settings.REST_API)
def send_get_request(url, headers=None, **kwargs):
    """Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param headers: Headers used for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: :class:`Response` object.
    """
    accept_json_header = {'accept': 'application/json'}
    headers = prepare_headers(headers, accept_json_header)
    return requests.get(url, headers=headers, **kwargs)


@base_request_url(settings.REST_API)
def send_post_request(url, headers=None, json=None, **kwargs):
    """Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param headers: Headers used for the new :class: `Request` object.
    :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: :class:`Response` object.
    """
    json_content_type_header = {'content-type': 'application/json'}
    headers = prepare_headers(headers, json_content_type_header)
    return requests.post(url, headers=headers, json=json, **kwargs)


@base_request_url(settings.REST_API)
def send_delete_request(url, **kwargs):
    """Sends a DELETE request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :returns: :class:`Response` object.
    """
    return requests.delete(url, **kwargs)


def prepare_headers(current_headers, obligatory_headers):
    """Adds `obligatory_headers` to `current_headers` if they are not already
    included.

    :param current_headers: Dict of original headers
    :param obligatory_headers: Dict of obligatory headers, which should be added
    :returns: dictionary of headers
    """
    if current_headers is None:
        headers = obligatory_headers
    else:
        for key, value in obligatory_headers.iteritems():
            if key not in current_headers:
                current_headers.update({key: value})
        headers = current_headers
    return headers