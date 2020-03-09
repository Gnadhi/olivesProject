from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from olives.models import Dish

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
    name = forms.CharField(label="Please enter a dish to add: ",max_length=50)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Dish
        fields = ('name',)

class DishDeleteForm(forms.ModelForm):
    dishs = Dish.objects.all()
    dish = []
    for d in dishs:
        dish += [(d.name,d.name)]
    dishDelete = forms.CharField(widget=forms.Select(choices=dish),help_text="Please select the dish to delete")

    class Meta:
        model = Dish
        fields = ('dishDelete',)
