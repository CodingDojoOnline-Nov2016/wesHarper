from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

import random, datetime
from .models import Leaderboard

# Create your views here.
def index(request):
	if 'activities' not in request.session:
		request.session['activities'] = []
	if 'gold_count' not in request.session:
		request.session['gold_count'] = 0
	return render(request, 'gold/index.html')

def process(request, location):
	if request.method == "POST":
		if 'gold_count' not in request.session:
			request.session['gold_count'] = 0
		if 'activities' not in request.session:
			request.session['activities'] = []

		locations = {
			"farm": ("won", random.randint(10, 20)),
			"cave": ("won", random.randint(5, 10)),
			"house": ("won", random.randint(2, 5)),
			"casino": ["", random.randint(-50, 50)],
		}

		for key, value in locations.items():
			if location == key:
				request.session['gold_count'] += value[1]
				if location == "casino":
					locations['casino'][0] = "won" if locations['casino'][1] >= 0 else "lost"
					if locations['casino'][0] == "won":
						exclam = "Nice"
						outcome = 1
					else:
						exclam = "Ouch"
						outcome = 0
					casino_str = "Entered the casino and {} {} golds... {}... {}".format(locations['casino'][0], locations['casino'][1], exclam, datetime.datetime.now())
					request.session['activities'].insert(0, (outcome, casino_str))
				else:
					outcome = 1
					string = "Earned {} golds from the {}! {}".format(value[1], location, datetime.datetime.now())
					request.session['activities'].insert(0, (outcome, string))
	return redirect(reverse('gold:index'))

def save(request):
	if request.method == "POST" and request.session['user_id']:

		data = {
			"score": request.session['gold_count'],
			"user_id": request.session['user_id'],
		}

		response = Leaderboard.objects.save_game(data)
		request.session['gold_count'] = 0
		request.session['activities'] = []

		messages.success(request, response)
	else:
		messages.error(request, "Oops! Something went wrong! Are you logged in?")
	return redirect(reverse('gold:index'))

def show(request):
	context = {
		'leaderboards': Leaderboard.objects.all().order_by('-top_score')[:15]
	}
	return render(request, 'gold/leaderboard.html', context)