from django.contrib import admin
from olives.models import Menu,Dish

admin.site.register(Menu)  # updates the registration to include this customised interface
admin.site.register(Dish) # Registers the model onto the admin website.
