from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, "survey/index.html")

def process(request):
	if request.method == "POST":
		print "*" * 50
		print request.POST
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
		try:
			request.session['submissions'] += 1
		except KeyError:
			request.session['submissions'] = 1
		return redirect('/results')
	else:
		return redirect('/')

def results(request):
	return render(request, "survey/results.html")