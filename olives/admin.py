from django.contrib import admin
from olives.models import Menu,Dishes

admin.site.register(Menu)  # updates the registration to include this customised interface
admin.site.register(Dishes) # Registers the model onto the admin website.
