from django.test import TestCase
from olives.forms import DishForm, StaffSignUpForm, ReviewForm, ContactForm, BookingForm

class TestForms(TestCase):



	def test_staffReg_form_valid_data(self):
		form = StaffSignUpForm(data={
			'username': 'test',
			'first_name': 'John',
			'last_name': 'Doe',
			'email': 'test@test.com',
			'password1': 'goldanddiamond1234',
			'password2': 'goldanddiamond1234',
			
			})

		self.assertTrue(form.is_valid())

	def test_dish_form_valid_data(self):
		form = DishForm(data={
			'name': 'brownie'
			})

		self.assertTrue(form.is_valid())