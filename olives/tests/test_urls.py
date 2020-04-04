from django.test import SimpleTestCase
from django.urls import reverse, resolve
from olives.views import confirmBooking, emailView, index, about_us, gallery, specialEvents, menu, booking, add_dish, delete_dish, staffSignUp, dishReview, reviewRest 

class TestUrls(SimpleTestCase):

	def test_index_url_is_resolved(self):
		url = reverse('olives:index')
		print(resolve(url))
		self.assertEquals(resolve(url).func, index)

	def test_about_url_is_resolved(self):
		url = reverse('olives:about-us')
		print(resolve(url))
		self.assertEquals(resolve(url).func, about_us)

	def test_gallery_url_is_resolved(self):
		url = reverse('olives:gallery')
		print(resolve(url))
		self.assertEquals(resolve(url).func, gallery)

	def test_specialEvents_url_is_resolved(self):
		url = reverse('olives:special-events')
		print(resolve(url))
		self.assertEquals(resolve(url).func, specialEvents)

	def test_menu_url_is_resolved(self):
		url = reverse('olives:menu')
		print(resolve(url))
		self.assertEquals(resolve(url).func, menu)

	def test_add_url_is_resolved(self): #
		url = reverse('olives:add_dish')
		print(resolve(url))
		self.assertEquals(resolve(url).func, add_dish)

	def test_delete_url_is_resolved(self):
		url = reverse('olives:delete_dish')
		print(resolve(url))
		self.assertEquals(resolve(url).func, delete_dish)

	def test_staffSignUp_url_is_resolved(self):
		url = reverse('olives:staffSignUp')
		print(resolve(url))
		self.assertEquals(resolve(url).func, staffSignUp)

	def test_contact_url_is_resolved(self):
		url = reverse('olives:contact-us')
		print(resolve(url))
		self.assertEquals(resolve(url).func, emailView)

	def test_confirmBooking_url_is_resolved(self):
		url = reverse('olives:confirm-booking')
		print(resolve(url))
		self.assertEquals(resolve(url).func, confirmBooking)

	def test_dishRev_url_is_resolved(self):
		url = reverse('olives:dishReview')
		print(resolve(url))
		self.assertEquals(resolve(url).func, dishReview)

	def test_restRev_url_is_resolved(self):
		url = reverse('olives:review-rest')
		print(resolve(url))
		self.assertEquals(resolve(url).func, reviewRest)


