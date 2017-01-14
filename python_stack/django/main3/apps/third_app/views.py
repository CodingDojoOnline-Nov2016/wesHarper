from django.shortcuts import render
from .models import People

# Create your views here.
def index(request):
	People.objects.create(first_name="Wes", last_name="Harper")
	people = People.objects.all()
	print people
	return render(request, "third_app/index.html")