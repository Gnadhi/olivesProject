from django.urls import path
from django.contrib import admin
from olives import views

app_name = "olives"

urlpatterns = [
    path("", views.index, name="index"),  # The index is the home page of the website
    path('about-us/', views.about_us, name='about-us'),  
    path('gallery/', views.gallery, name='gallery'),
    path("booking/", views.booking, name="booking"),

    path('special-events/', views.specialEvents, name='special-events'),
    path("review-dish/", views.dishReview, name="dishReview"),
    path("staff-sign-up/", views.staffSignUp, name="staffSignUp"),
    path('admin/', admin.site.urls, name="admin"),
    path("add-dish/", views.add_dish, name="add_dish"),
    path("delete-dish/", views.delete_dish, name="delete_dish"),
    path("staff-register/", views.staffSignUp, name="staff_signup"),
    path("staff/", views.staffData, name="staff"),
    path('contact-us/', views.emailView, name='contact-us'),

    path("menu/", views.menu, name="menu"),
    path("review/", views.reviewRest, name="review-rest"),
    path("confirm-booking/", views.confirmBooking, name="confirm-booking"),

]
