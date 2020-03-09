from django.urls import path
from django.contrib import admin
from olives import views

app_name = "olives"

urlpatterns = [
    path("", views.index, name="index"),  # The index is the home page of the website
    path("dish-review/", views.dishReview, name="dishReview"),
    path("staff-sign-up/", views.staffSignUp, name="staffSignUp"),
    path('admin/', admin.site.urls, name="admin"),
    path("add_dish/", views.add_dish, name="add_dish"),
    path("booking/", views.make_booking, name="booking"),
    path("delete_dish/", views.delete_dish, name="delete_dish"),
]
