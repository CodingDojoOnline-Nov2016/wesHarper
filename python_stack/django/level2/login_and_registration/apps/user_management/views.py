from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'user_management/index.html')

def success(request):
	return render(request, 'user_management/success.html')

def create(request):
	return redirect('/success')

def login(request):
	return redirect('/success')