from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # PLACEHOLDER !!!
    response = render(request, "base.html")
    return response
