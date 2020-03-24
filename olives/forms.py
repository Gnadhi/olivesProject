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

    class Meta:
        model = Dish
        fields = ('name',)

    def clean(self):
        data = self.cleaned_data
        name = data.get('name')
        # to check for unquie dishes
        dishes_same_name = Dish.objects.filter(name__icontains=name).count()
        if(dishes_same_name>0):
            self.add_error('name','Dish already exists!')



class BookingForm(forms.ModelForm):
    # For the booking form doesnt have the confirm field as that is always set to false initially
    name = forms.CharField(max_length=128, help_text="Name")
    email = forms.EmailField(help_text="Email Address")
    phone = forms.CharField(max_length=15, help_text="Phone Number")
    noOfPeople = forms.IntegerField(help_text="Number of People")
    date = forms.DateField(help_text="Date")
    time = forms.TimeField(help_text="Time")

    class Meta:
        model = Booking
        fields = ("name", "phone", "noOfPeople", "date", "time")


class DishDeleteForm(forms.Form):
    
    dishDelete = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(DishDeleteForm, self).__init__(*args, **kwargs)
        self.fields['dishDelete'] = forms.ChoiceField(choices=[(dish.id,dish.name) for dish in Dish.objects.all() ],help_text="Select Dish to Delete")
