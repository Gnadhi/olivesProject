from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from olives.forms import StaffSignUpForm, BookingForm
from olives.models import Dish
from olives.forms import DishForm, DishDeleteForm
from django.contrib import messages
from django.views import View


def index(request):
    # PLACEHOLDER !!!
    response = render(request, "olives/base.html")
    return response


def dishReview(request):
    dishList = Dish.objects.order_by('-likes')[:5]
    allDishList = Dish.objects.all()
    context_dict = {}
    context_dict['boldmessage'] = 'The top five dishes of Olives & Pesto:'
    context_dict['TopDishes'] = dishList
    context_dict['AllDishes'] = allDishList
    response = render(request, "olives/reviewDishes.html",context=context_dict)
    return response


def add_dish(request):
    form = DishForm()

    if request.method == 'POST':
        form = DishForm(request.POST)

        if form.is_valid():
            if(Dish.objects.filter(name=form.cleaned_data['name']).exists()==False):
                form.save(commit=True)
                return redirect('/olives/dish-review')
            else:
                messages.warning(request,'The dish already exists!')
                render(request, 'olives/add_dish.html', {'form':form})
        else:
            print(form.errors)
    return render(request, 'olives/add_dish.html', {'form': form})

def delete_dish(request):
    form = DishDeleteForm(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            dish = form.cleaned_data.get('dishDelete')
            Dish.objects.filter(name=dish).delete()
            return redirect('/olives/dish-review')
        else:
            print(form.errors)
    return render(request,'olives/delete_dish.html',{'form':form})

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
