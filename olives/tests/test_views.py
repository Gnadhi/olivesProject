from django.test import TestCase, Client
from django.urls import reverse, resolve
from olives.models import Menu, Review, Dish, Customer, Staff
import json
#from olives.views import menu


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.menu_url = reverse('olives:menu')
		self.booking_url = reverse('olives:booking')

	def test_menu_GET(self):

		response = self.client.get(self.menu_url)

		self.assertEquals(response.status_code, 200) # Asserts we should be able to access this view. 
		self.assertTemplateUsed(response, 'olives/menu.html')
		# Specifies the template that should be used for this view. 

	def test_booking_GET(self):
		response = self.client.get(self.booking_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'olives/booking.html')

	def test_contact_GET(self):
		response = self.client.get(self.booking_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'olives/booking.html')

