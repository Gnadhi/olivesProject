from django.test import TestCase, Client
from django.urls import reverse, resolve
#from olives.models import Menu, Review, Dish, Customer, Staff
import json
#from olives.views import menu


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.menu_url = reverse('olives:menu')#
		self.booking_url = reverse('olives:booking')#
		self.contact_url = reverse('olives:contact-us')#
		self.index_url = reverse('olives:index')
		self.about_url = reverse('olives:about-us')
		self.gallery_url = reverse('olives:gallery')
		self.special_url = reverse('olives:special-events')
		self.add_url = reverse('olives:add_dish')
		self.delete_url = reverse('olives:delete_dish')
		self.staffReg_url = reverse('olives:staffSignUp')
		self.confirmBook_url = reverse('olives:confirm-booking')



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
		response = self.client.get(self.contact_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'olives/contactus.html')
		
	def test_index_GET(self):
		response = self.client.get(self.index_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'olives/index.html')

	def test_about_GET(self):
		response = self.client.get(self.about_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'olives/about-us.html')

	def test_gallery_GET(self):
		response = self.client.get(self.gallery_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'olives/gallery.html')

	def test_special_GET(self):
		response = self.client.get(self.special_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'olives/special-events.html')


	def test_staffSignUp_GET(self):
		response = self.client.get(self.staffReg_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'olives/staffRegister.html')


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Confirm booking, add and remove dish pages act as form post re-direct actions, therefore they are 302, not 200. 