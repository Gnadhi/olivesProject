from django.test import SimpleTestCase
from django.urls import reverse, resolve
from olives.views import index, about_us, gallery, specialEvents

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