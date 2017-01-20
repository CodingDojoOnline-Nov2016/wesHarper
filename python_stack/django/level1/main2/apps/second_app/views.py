from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		"email": "blob@gmail.com",
		"name": "Mike",
	}
	return render(request, "second_app/index.html", context)

def show(request, user_id):
	print "*" * 50
	print user_id
	context = {
		"id": user_id,
	}
	return render(request, "second_app/show.html", context)