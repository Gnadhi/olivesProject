from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from olives.models import Review, Dish, Customer, Staff, Booking


class TestModels(TestCase):

	def setUp(self):

		self.booking1 = Booking.objects.create(
			name = 'test',
			email = 'test@test.com',
			phone = '0000 0000',
			noOfPeople = 1,
			date = '2020-09-01',
			time = '14:00:00',
			)

		self.dish1 = Dish.objects.create(
			name = 'test',
			likes = 0,
			)

		self.customer1 = User.objects.create_user(
			username='test_customer', 
			email='test_user@gmail.com', 
			password='top_secret', 
			is_staff = False
			)

		self.review1 = Review.objects.create(
			user = self.customer1,
			review = 'good'
			)


	def test_booking(self):
		self.assertEqual(self.booking1.name, 'test')
		self.assertEqual(self.booking1.email, 'test@test.com')
		self.assertEqual(self.booking1.phone, '0000 0000')
		self.assertEqual(self.booking1.noOfPeople, 1)
		self.assertEqual(self.booking1.date, '2020-09-01')
		self.assertEqual(self.booking1.time, '14:00:00')

	def test_dish(self):
		self.assertEqual(self.dish1.name, 'test')
		self.assertEqual(self.dish1.likes, 0)

	def test_review(self):
		self.assertEqual(self.review1.user, self.customer1)
		self.assertEqual(self.review1.review, "good")

