import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'olivesProject.settings')

import django

django.setup()
from olives.models import Dishes


def populate():
    dishes = [
        {'name': 'Pav Bhaji', 'likes': 100, 'dislike': 3},
        {'name': 'Pani Puri', 'likes': 300, 'dislike': 10},
        {'name': 'Masala Dosa', 'likes': 153, 'dislike': 32},
        {'name': 'Paneer Butter Masala', 'likes': 654, 'dislike': 12},
        {'name': 'Kadhai Paneer', 'likes': 123, 'dislike': 36},
        {'name': 'Tadka Dal', 'likes': 459, 'dislike': 45},
        {'name': 'Dal Makhani', 'likes': 157, 'dislike': 100}]
    for i in range(0, len(dishes)):
        add_dishes(dishes[i]['name'], dishes[i]['likes'], dishes[i]['dislike'])
    for d in Dishes.objects.all():
        print(f'- {d}')


def add_dishes(name, likes, dislike):
    d = Dishes.objects.get_or_create(name=name, likes=likes, dislike=dislike)[0]
    d.save()
    return d


if __name__ == '__main__':
    print('Starting Olive Dish Population Script...')
    populate()
