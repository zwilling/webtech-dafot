from django.shortcuts import render


def index(request):
    """
    Main page view. Generates index.html template.

    :param: :class: `Request` object
    :returns: :class: `HTTPResponse` object
    """
    return render(request, "main/index.html")


def our_team(request):
    """
    Team members view. Generates our_team.html template.

    :param: :class: `Request` object
    :returns: :class: `HTTPResponse` object
    """
    return render(request, "main/our_team.html")


def coming(request):
    """
    Coming soon view. Generates coming.html template.

    :param: :class: `Request` object
    :returns: :class: `HTTPResponse` object
    """
    return render(request, "main/coming.html")