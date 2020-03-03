import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "olivesProject.settings")

import django

django.setup()

from olives.models import Menu


def populate():
    menus = [
        {"name": "Official Python Tutorial",
         "description": "http://docs.python.org/3/tutorial/"},
        {"name": "How to Think like a Computer Scientist",
         "description": "http://www.greenteapress.com/thinkpython/"}
    ]

    for menu in menus:
        m = add_menu(menu["name"], menu["description"])

    for menu in Menu.objects.all():
            print(f"- {menu}")


def add_menu(name, description, image=None, file=None):
    p = Menu.objects.get_or_create(name=name, description=description)[0]
    p.image = image
    p.fie = file
    p.save()
    return p


# Start execution here
if __name__ == "__main__":
    print("Starting Olives - Menu Model populate script...")
    populate()
