from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def our_team(request):
    return render(request, "main/our_team.html")


def coming(request):
    return render(request, "main/coming.html")