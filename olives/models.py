import os

from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    # Note in the database only the stores the url to these items and not the items themselves
    # Note it will store it in the MEDIA/ folder
    image = models.ImageField(upload_to=os.path.join("menus", "images"))
    file = models.FileField(upload_to=os.path.join("menus", "files"))

    class Meta:
        verbose_name_plural = 'Menu'

class Dishes(models.Model):
    name = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural='Dishes'

    def __str__(self):
        return self.name