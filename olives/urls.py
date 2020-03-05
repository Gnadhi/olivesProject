from django.urls import path
from django.contrib import admin
from olives import views

app_name = "olives"

urlpatterns = [
<<<<<<<
    path("", views.index, name="index"),  # The index is the home page of the website
    path("dish-review/", views.dishReview, name="dishReview"),
    path("staff-sign-up/", views.staffSignUp, name="staffSignUp")
=======
    path('admin/', admin.site.urls, name = "admin"),
    path('index/', views.index, name = 'index'),  # The index is the home page of the website
    path("dish-review/", views.dishReview, name = "dishReview"),
    
>>>>>>>
]
