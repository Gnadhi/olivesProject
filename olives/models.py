import os

from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    # Note in the database only the stores the url to these items and not the items themselves
    # Note it will store it in the MEDIA/ folder
    image = models.ImageField(upload_to=os.path.join("menus", "images"))
    file = models.FileField(upload_to=os.path.join("menus", "files"))
