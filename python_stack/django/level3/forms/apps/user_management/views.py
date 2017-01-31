from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .forms import RegisterForm
# Create your views here.
def index(req):
	# Instantiate form classes from forms.py
	reg_form = RegisterForm()
	# log_form = LoginForm()
	# Assign forms to context dictionary for use in index
	context = { 
		"reg_form": reg_form,
		# "log_form": log_form,
		"title": "Login or Register",
	}

	return render(req, "user_management/index.html", context)

def login(req):
	pass

def create(req):
	# Confirm the proper HTTP method for security and to avoid bad routes
	if req.method == "POST":
		# Bind the post data to an instance of the form
		bound_form = RegisterForm(req.POST)
		# Test bound_form using built-ins
		if bound_form.is_valid():
			pass
		else:
			print bound_form.errors
			errors = bound_form.errors
			for error in errors:
				messages.error(req, error[0])

	return redirect(reverse('users:index'))

def logout(req):
	pass