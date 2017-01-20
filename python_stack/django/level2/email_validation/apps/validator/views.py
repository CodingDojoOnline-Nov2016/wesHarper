from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserManager, User

# Create your views here.
def index(request):
	return render(request, 'validator/index.html')

def process(request):
	print request.POST['email']

	valid, response = User.objects.validate_email(request.POST['email'])
	if valid:
		User.objects.create(email=response)
		messages.success(request, "Congrats, you entered the following valid email address: {}".format(response))
		return redirect('/success')
	else:
		print valid
		for error in response:
			messages.error(request, error)
		return redirect('/')

def success(request):
	users = User.objects.all()
	context = {
		"users": users,
	}
	return render(request, 'validator/success.html', context)

def destroy(request, id):
	User.objects.get(id=id).delete()
	return redirect('/success')