import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'olivesProject.settings')

import django

django.setup()
from olives.models import Dish


def populate():
    dishes = [
        {'name': 'Pav Bhaji', 'likes': 100},
        {'name': 'Pani Puri', 'likes': 300},
        {'name': 'Masala Dosa', 'likes': 153},
        {'name': 'Paneer Butter Masala', 'likes': 654},
        {'name': 'Kadhai Paneer', 'likes': 123},
        {'name': 'Tadka Dal', 'likes': 459},
        {'name': 'Dal Makhani', 'likes': 157}]
    for i in range(0, len(dishes)):
        add_dishes(dishes[i]['name'], dishes[i]['likes'])
    for d in Dish.objects.all():
        print(f'- {d}')


def add_dishes(name, likes):
    d = Dish.objects.get_or_create(name=name, likes=likes)[0]
    d.save()
    return d


if __name__ == '__main__':
    print('Starting Olive Dish Population Script...')
    populate()
