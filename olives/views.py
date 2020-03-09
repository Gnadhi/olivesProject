from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from olives.forms import StaffSignUpForm, BookingForm
from olives.models import Dish
from olives.forms import DishForm


def index(request):
    # PLACEHOLDER !!!
    response = render(request, "olives/base.html")
    return response


def dishReview(request):
    dishList = Dish.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'The top five dishes of Olives & Pesto:'
    context_dict['TopDishes'] = dishList
    response = render(request, "olives/reviewDishes.html", context=context_dict)
    return response


def add_dish(request):
    form = DishForm()

    if request.method == 'POST':
        form = DishForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/olives/')
        else:
            print(form.errors)
    return render(request, 'olives/add_dish.html', {'form': form})


def staffSignUp(request):
    if request.method == 'POST':
        form = StaffSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect("olives:index")
    else:
        form = StaffSignUpForm()
    return render(request, 'olives/staffRegister.html', {'form': form})


def make_booking(request):
    form = BookingForm()

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("olives:index")
        else:
            print(form.errors)

    return render(request, "olives/booking.html", {'form': form})
