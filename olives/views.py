from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # PLACEHOLDER !!!
    response = render(request, "olives/base.html")
    return response


def dishReview(request):
    response = render(request, "olives/reviewDishes.html")
    return response
