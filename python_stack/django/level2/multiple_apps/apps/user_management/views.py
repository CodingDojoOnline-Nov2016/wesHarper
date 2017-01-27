from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from .models import User
# Create your views here.
def index(request):
	return render(request, 'user_management/index.html')

def success(request):
	return render(request, 'user_management/success.html')

def create(request):
	if request.method == "POST":
		valid, response = User.objects.validate_and_add(request.POST)
		if valid:
			messages.success(request, "Hello {} {}!".format(response.first_name, response.last_name))
			request.session['user_id'] = response.id
			return redirect(reverse('gold:index'))
		else:
			for error in response:
				messages.error(request, error)

	return redirect(reverse('user_management:index'))

def login(request):
	if request.method == "POST":
		valid, response = User.objects.login_check(request.POST)
		if valid:
			messages.success(request, "Hello {} {}, thanks for logging in!".format(response.first_name, response.last_name))
			request.session['user_id'] = response.id
			return redirect(reverse('gold:index'))
		else:
			for error in response:
				messages.error(request, error)
	
	return redirect(reverse("user_management:index"))

def logout(request):
	request.session.clear()
	return redirect(reverse('gold:index'))