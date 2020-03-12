from django.http import HttpResponse, HttpResponseRedirect
from olives.forms import StaffSignUpForm, BookingForm
from olives.models import Dish, Staff
from olives.forms import DishForm, DishDeleteForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User

def index(request):
    return render(request, "olives/index.html")


def about(request):
    return render(request, "olives/about.html")


def gallery(request):
    return render(request, "olives/gallery.html")


def specialEvents(request):
    return render(request, "olives/special-events.html")


def dishReview(request):
    dishList = Dish.objects.order_by('-likes')[:5]
    allDishList = Dish.objects.all()
    context_dict = {}
    context_dict['boldmessage'] = 'The top five dishes of Olives & Pesto:'
    context_dict['TopDishes'] = dishList
    context_dict['AllDishes'] = allDishList
    response = render(request, "olives/reviewDishes.html", context=context_dict)
    return response


def add_dish(request):
    form = DishForm()

    if request.method == 'POST':
        form = DishForm(request.POST)

        if form.is_valid():
            if (Dish.objects.filter(name=form.cleaned_data['name']).exists() == False):
                form.save(commit=True)
                return redirect('/olives/add_dish')
            else:
                messages.warning(request, 'The dish already exists!')
                render(request, 'olives/add_dish.html', {'form': form})
        else:
            render(request, 'olives/add_dish.html', {'form': form})
            print(form.errors)
    return render(request, 'olives/add_dish.html', {'form': form})


def delete_dish(request):
    if request.method == 'POST':
        form = DishDeleteForm(request.POST)
        if form.is_valid():
            dishID = form.cleaned_data.get('dishDelete')
            dish = Dish.objects.filter(id=dishID).first().delete()
            return HttpResponseRedirect(reverse('olives:delete_dish'))
        else:
            print(form.errors)
    else:
        form = DishDeleteForm()
    return render(request, 'olives/delete_dish.html', {'form': form})


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


def staffData(request):
    user_list = User.objects.all()
    context_dict = {}
    context_dict['users'] = user_list
    return render(request, 'olives/staff.html', context=context_dict)

def make_booking(request):
    form = BookingForm()

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # Sets up Email details
            mail_subject = "Booking Request Received"
            mail_body = "A booking request has been received with the following details a confirmation email will be " \
                        "sent shortly. " + "\n" \
                        + "Name: " + form.cleaned_data.get("name") + "\n" \
                        + "Phone: " + form.cleaned_data.get("phone") + "\n" \
                        + "Number of People: " + str(form.cleaned_data.get("noOfPeople")) + "\n" \
                        + "Date: " + str(form.cleaned_data.get("date")) + "\n" \
                        + "Time: " + str(form.cleaned_data.get("time")) + "\n"
            mail_sender = "Booking@olivesandpesto.com"
            mail_sendAddress = form.cleaned_data.get("email")
            # Send Mail takes 4  required parameters - Subject Line, Message Body, Sender Address, Send Address
            send_mail(mail_subject, mail_body, mail_sender, [mail_sendAddress], fail_silently=False, )
            return redirect("olives:index")
        else:
            print(form.errors)

    return render(request, "olives/booking.html", {'form': form})


