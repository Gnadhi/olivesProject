from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from olives.models import Dish, Booking


class StaffSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    isAdmin = forms.BooleanField(help_text="If Admin then Yes ")
    isSuperuser = forms.BooleanField(help_text="If SuperUser then Yes")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', "isAdmin", "isSuperuser")


class DishForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text="Please enter the name of the dish.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Dish
        fields = ('name',)


class BookingForm(forms.ModelForm):
    # For the booking form doesnt have the confirm field as that is always set to false initially
    name = forms.CharField(max_length=128, help_text="Please enter your name")
    phone = forms.CharField(max_length=15, help_text="Please enter your phone number")
    noOfPeople = forms.IntegerField(help_text="Please enter the number of people you want to book a table for")
    date = forms.DateField(help_text="Please enter the date of booking")
    time = forms.TimeField(help_text="Please enter the time of booking")

    class Meta:
        model = Booking
        fields = ("name", "phone", "noOfPeople", "date", "time")
