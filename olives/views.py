from django.http import HttpResponse, HttpResponseRedirect

from olives.forms import StaffSignUpForm, BookingForm
from olives.models import Dish, Staff

from olives.forms import StaffSignUpForm, BookingForm, ReviewForm
from olives.models import Dish, Staff, Review, Booking, LikedDish

from olives.forms import DishForm, DishDeleteForm, ContactForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import make_password  # This is to allow encryption of the passwords.
from static.ML.review import reviewModel
from static.ML.review.reviewModel import use_model

def index(request):
	return render(request, "olives/index.html")


def about_us(request):
	return render(request, "olives/about-us.html")


# This checks if the user is a staff member.
def staff_check(user):
	return user.is_authenticated and user.is_staff


def gallery(request):
	return render(request, "olives/gallery.html")


def specialEvents(request):
	return render(request, "olives/special-events.html")


# This is available to all logged in users.
@login_required


# This is available to all logged in users.
# This allows custom testss

def dishReview(request):
	# Adds 1 when button is clicked, to the likes variable of the dish object.
	# The second if condition checks whether the user has already liked the dish.
	if request.method == 'POST':
		dishId = request.POST['dish-id']
		dish = Dish.objects.filter(id=dishId).first()
		if LikedDish.objects.filter(userID=request.user.id, dishID=dishId).exists()==False:
			dish.likes += 1
			dish.save()
			likeUser = LikedDish()
			likeUser.dishID = dishId
			likeUser.userID = request.user.id
			likeUser.save()

	dishList = Dish.objects.order_by('-likes')[:5]
	allDishList = Dish.objects.all()
	context_dict = {}
	context_dict['boldmessage'] = 'The top five dishes of Olives & Pesto:'
	context_dict['TopDishes'] = dishList
	context_dict['AllDishes'] = allDishList
	response = render(request, "olives/reviewDishes.html", context=context_dict)
	return response


# This is for the admin(s) only
@login_required
def reviewRest(request):
	review = Review.objects.all()
	context_dict = {'userReviews': review}
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			form.instance.user = request.user
			score = use_model(form.instance.review)
			form.instance.score = score
			form.save(commit=True)
			return HttpResponseRedirect(reverse('olives:review-rest'))
		else:
			print(form.errors)
	else:
		form = ReviewForm()
	context_dict.update({"form": form})
	return render(request, 'olives/review.html', context=context_dict)


# This is for the admin(s) only
@user_passes_test(staff_check)

def add_dish(request):
	if request.method == 'POST':
		form = DishForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect(reverse('olives:add_dish'))
		else:
			print(form.errors)
	else:
		form = DishForm()
	return render(request, 'olives/add_dish.html', {'form': form})


# This is for the admin(s) only.
@login_required


# This is for the admin(s) only.
@user_passes_test(staff_check)

def delete_dish(request):
	if request.method == 'POST':
		form = DishDeleteForm(request.POST)
		if form.is_valid():
			dishID = form.cleaned_data.get('dishDelete')
			dish = Dish.objects.filter(id=dishID).first().delete()
			return HttpResponseRedirect(reverse('olives:delete_dish'))
		else:
			print(form.errors)
	else:
		form = DishDeleteForm()
	return render(request, 'olives/delete_dish.html', {'form': form})

def staffSignUp(request):
	if request.method == 'POST':
		form = StaffSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			# Encrypting the password using Argon2 before storing it
			raw_password = form.cleaned_data.get('password1')
			hashed_password = make_password(raw_password)
			user = authenticate(username=username, password=hashed_password)
			# login(request, user)
			return redirect("olives:index")
	else:
		form = StaffSignUpForm()
	return render(request, 'olives/staffRegister.html', {'form': form})


# This is for Admins and SUPERUSERS only.
@login_required


# This is for Admins and SUPERUSERS only.
@user_passes_test(staff_check)

def staffData(request):
	user_list = User.objects.all()
	context_dict = {}
	context_dict['users'] = user_list
	return render(request, 'olives/staff.html', context=context_dict)


def booking(request):
	form = BookingForm()

	if request.method == "POST":
		form = BookingForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			# Sets up Email details
			mail_subject = "Booking Request Received"
			mail_body = "A booking request has been received with the following details a confirmation email will be " \
						"sent shortly. " + "\n" \
						+ "Name: " + form.cleaned_data.get("name") + "\n" \
						+ "Phone: " + form.cleaned_data.get("phone") + "\n" \
						+ "Number of People: " + str(form.cleaned_data.get("noOfPeople")) + "\n" \
						+ "Date: " + str(form.cleaned_data.get("date")) + "\n" \
						+ "Time: " + str(form.cleaned_data.get("time")) + "\n"
			mail_sender = "Booking@olivesandpesto.com"
			mail_sendAddress = form.cleaned_data.get("email")
			# Send Mail takes 4  required parameters - Subject Line, Message Body, Sender Address, Send Address
			send_mail(mail_subject, mail_body, mail_sender, [mail_sendAddress], fail_silently=False)
			return redirect("olives:index")
		else:
			print(form.errors)

	return render(request, "olives/booking.html", {'form': form})




def emailView(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:

				send_mail(subject, message, from_email, ['olivesandpesto1234@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('success')
	return render(request, "olives/contactus.html", {'form': form})

def successView(request):
	return redirect("olives:index")


def menu(request):
	return render(request, "olives/menu.html")


@user_passes_test(staff_check)
def confirmBooking(request):
	if request.method == 'POST':
		# Updates database
		bookingId = request.POST['confirm-booking']
		booking = Booking.objects.filter(id=bookingId).first()
		booking.confirm = True
		booking.save()
		# sends booking confirmation
		mail_subject = "Booking Request Confirmed"
		mail_body = "We have confirmed a booking with the following details " + "\n" \
					+ "Name: " + booking.name + "\n" \
					+ "Phone: " + booking.phone + "\n" \
					+ "Number of People: " + str(booking.noOfPeople) + "\n" \
					+ "Date: " + str(booking.date) + "\n" \
					+ "Time: " + str(booking.time) + "\n"
		mail_sender = "Booking@olivesandpesto.com"
		mail_sendAddress = booking.email
		# Send Mail takes 4  required parameters - Subject Line, Message Body, Sender Address, Send Address
		send_mail(mail_subject, mail_body, mail_sender, [mail_sendAddress], fail_silently=False)


	bookings = Booking.objects.order_by('time')
	context_dict = {}
	context_dict['bookings'] = bookings
	return render(request, "olives/confirm-booking.html", context=context_dict)

