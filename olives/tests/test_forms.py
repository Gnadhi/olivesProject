from django.test import SimpleTestCase
from olives.forms import DishForm, StaffSignUpForm, ReviewForm, ContactForm, BookingForm

class TestForms(SimpleTestCase):

	def test_contact_form_valid_data(self):
		form = ContactForm(data={
			'from_email': 'test@test.com',
			'subject': 'test',
			'message': 'test',
			})

		self.assertTrue(form.is_valid()) # Form should be valid if all fields satisfied. 

	def test_contact_form_no_data(self): # Form with no data must be invalid
		form = ContactForm(data={}) 

		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 3)

	def test_booking_form_valid_data(self):
		form = BookingForm(data={
			'name': 'test',
			'email': 'test@test.com',
			'phone': '0000 0000',
			'noOfPeople': 2,
			'date': '2020-09-01',
			'time': '14:00:00'
			})
		self.assertTrue(form.is_valid())

	def test_booking_form_no_data(self):
		form = BookingForm(data={})

		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 6)

	def test_review_form_valid_data(self):
		form = ReviewForm(data={
			'review': 'test review'
			})
		self.assertTrue(form.is_valid())

	def test_review_form_no_data(self):
		form = ReviewForm(data={})

		self.assertFalse(form.is_valid())
		self.assertEquals(len(form.errors), 1)

	




