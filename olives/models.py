import os  # Needed to use the os.path function

from django.db import models  # Needed to uses django models
from django.template.defaultfilters import slugify  # Needed to uses the slugify function
from django.contrib.auth.models import User, AbstractUser  # Needed to create a 1 to 1 link with the django built in


# User model


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    slug = models.CharField(max_length=50, null=True)
    # Note in the database only the stores the url to these items and not the items themselves
    # Note it will store it in the MEDIA/ folder
    image = models.ImageField(upload_to=os.path.join("menus", "images"))
    file = models.FileField(upload_to=os.path.join("menus", "files"))

    def save(self, *args, **kwargs):  # save method is always called when creating or updating an instance of Django
        # model
        self.slug = slugify(self.name)  # slugify creates a url safe name by removing the spaces for dashes
        super(Menu, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Menus'

# Contains the reviews provided by the users and staff.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Review'    

# Contains all the dishes provided by the restaurant.
class Dish(models.Model):
    name = models.CharField(max_length=50)  # The name of the dish
    likes = models.IntegerField(default=0)  # The number of likes the dishes have

    class Meta:
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name

# Keeps track of the users and the dishes liked by them.
class LikedDish(models.Model):
    userID = models.IntegerField(default=0)
    dishID = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'LikedDish'

# Order has a many to many relationship with dishes
class Order(models.Model):
    orderId = models.CharField(max_length=64)
    dishes = models.ManyToManyField(Dish)  # Creates the many to many link with the dishes table

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.orderId


# Order has many to 1 relationship with Customer
class Customer(models.Model):
    # This line is required as it links user profile to a user model instance.
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.customer


class Staff(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_staff = True
    staff_list = User.objects.all()

    class Meta:
        verbose_name_plural = 'Staff'

    def __str__(self):
        return self.staff

class Admin(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    admin_check = models.ForeignKey(Staff, on_delete=models.CASCADE)
    is_admin = True

# Booking no longer has a link to any other table
class Booking(models.Model):
    name = models.CharField(max_length=128, default="")
    email = models.EmailField(default="")
    phone = models.CharField(max_length=15)
    noOfPeople = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    confirm = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return self.name

