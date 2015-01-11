from django.shortcuts import render


def bad_request(request):
    values_for_template = {}
    return render(request, 'errors/400.html', values_for_template, status=400)


def permission_denied(request):
    values_for_template = {}
    return render(request, 'errors/403.html', values_for_template, status=403)


def page_not_found(request):
    values_for_template = {}
    return render(request, 'errors/404.html', values_for_template, status=404)


def server_error(request):
    values_for_template = {}
    return render(request, 'errors/500.html', values_for_template, status=500)