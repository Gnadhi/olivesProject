from django.urls import path
from olives import views

app_name = "olives"

urlpatterns = [
    path("", views.index, name="index"),  # The index is the home page of the website
    path("dish-review/", views.dishReview, name="dishReview"),
]
