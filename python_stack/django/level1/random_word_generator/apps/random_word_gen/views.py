from django.shortcuts import render, redirect
import random, string
# Create your views here.
def index(request):
	print "*" * 50
	print 'rand_word' in request.session
	if not 'rand_word' in request.session:
		request.session['rand_word'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(15))
	if not 'attempt' in request.session:
		request.session['attempt'] = 1
	return render(request, 'random_word_gen/index.html')

def random_word(request):
	if request.method == "POST":
		request.session['rand_word'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(15))
		try:
			request.session['attempt'] += 1
		except KeyError:
			request.session['attempt'] = 1
		return redirect('/')
	else:
		return redirect('/')
