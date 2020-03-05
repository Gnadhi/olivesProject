from django.contrib import admin
from olives.models import Menu, Dish, Order, Booking, Customer, Staff


# adds class that will automatically fill the slug field
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Menu, MenuAdmin)  # Updates the registration to include this customised interface

admin.site.register(Dish)  # Registers the model onto the admin website.
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Booking)

admin.site.register(Staff)
