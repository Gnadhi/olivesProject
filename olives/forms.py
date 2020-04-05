from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from olives.models import Dish, Booking, Review
from datetime import datetime
from django.utils import timezone

class StaffSignUpForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    is_staff = True
    class Meta:
        model = User
        fields = ('username', "first_name", "last_name", 'email', 'password1', 'password2', "is_staff")

class ReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Review
        fields = ('review',)
    

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('name',)

    def clean(self):
        data = self.cleaned_data
        name = data.get('name')
        # to check for unique dishes
        if (Dish.objects.filter(name__icontains=name)):
            self.add_error('name', 'Dish already exists!')


class BookingForm(forms.ModelForm):
    # For the booking form doesnt have the confirm field as that is always set to false initially
    name = forms.CharField(max_length=128, help_text="Name")
    email = forms.EmailField(help_text="Email Address")
    phone = forms.CharField(max_length=15, help_text="Phone Number")
    noOfPeople = forms.IntegerField(help_text="Number of People")

    date = forms.DateField(help_text="Date")

    date = forms.DateField(widget=forms.SelectDateWidget, help_text="Date")

    time = forms.TimeField(help_text="Time")

    class Meta:
        model = Booking
        fields = ("name", "phone", "noOfPeople", "date", "time")

    
    def clean(self):
        data = self.cleaned_data
        if(data['noOfPeople']<=1):
            self.add_error('noOfPeople', "People cannot be 0 or negative")
        if data['date'] < timezone.now().date():
            self.add_error('date',"Date cannot be in the past!")
        elif data['date'] == timezone.now().date() and data['time'] < datetime.now().time():
            self.add_error('time',"Time cannot be in past!")
        


class DishDeleteForm(forms.Form):
    dishDelete = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(DishDeleteForm, self).__init__(*args, **kwargs)

        self.fields['dishDelete'] = forms.ChoiceField(choices=[(dish.id,dish.name) for dish in Dish.objects.all() ],help_text="Select Dish to Delete")

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


