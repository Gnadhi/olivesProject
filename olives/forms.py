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

    class Meta:
        model = Dish
        fields = ('name',)

class DishDeleteForm(forms.Form):
    
    dishDelete = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(DishDeleteForm, self).__init__(*args, **kwargs)
        self.fields['dishDelete'] = forms.ChoiceField(choices=[(dish.id,dish.name) for dish in Dish.objects.all() ])
