from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from olives.forms import StaffSignUpForm


def index(request):
    # PLACEHOLDER !!!
    response = render(request, "olives/base.html")
    return response


def dishReview(request):
    response = render(request, "olives/reviewDishes.html")
    return response


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
