from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from olives.models import Menu, Dish, Booking, Customer, Staff, Admin, Review

#Staff model yet to fixed.

# from django.contrib.auth.admin import UserAdmin
#from .models import User


# adds class that will automatically fill the slug field
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

# class StaffInLine(admin.StackedInline):
#     model = Staff
#     can_delete = False
#     if Admin.is_admin == True:
#         can_delete = True
#     else:
#         can_delete = False
#     print(can_delete)
#     verbose_name_plural = 'Staff'

# class AdminInLine(admin.StackedInline):
#     model = Admin
#     can_delete = True
#     verbose_name_plural = 'Admin'

# class UserAdmin(BaseUserAdmin):
#     inlines = (StaffInLine,)


# admin.site.register(User, UserAdmin)

admin.site.register(Menu, MenuAdmin)  # Updates the registration to include this customised interface

admin.site.register(Dish)  # Registers the model onto the admin website.
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Review)
# This is to Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User)


#admin.site.register(Staff)
