from flask import Flask, redirect, session, render_template, request
app = Flask(__name__)

app.secret_key = "this is a secret"

@app.route('/')
def index():
	return render_template('index.html', title="Ninja Gold!")

@app.route('/process_money', methods=['POST'])
def process_money():
	import random, datetime

	try:
		session['building'] = session['building']
	except KeyError:
		session['gold_count'] = 0
		session['building'] = []
		session['time'] = []
		session['amt'] = []

	place = request.form['building']
	amt = 0;

	if place == 'farm':
		amt = random.randrange(10, 20 + 1)
	elif place == 'cave':
		amt = random.randrange(5, 10 + 1)
	elif place == 'house':
		amt = random.randrange(2, 5 + 1)
	elif place == 'casino':
		amt = random.randrange(-50, 50 + 1)

	session['gold_count'] += amt
	session['building'].insert(0, place)
	session['time'].insert(0, datetime.datetime.now())
	session['amt'].insert(0, amt)

	print session['gold_count'], session['building'], session['time'], session['amt'], "<-----------------------"

	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	session['gold_count'] = 0
	return redirect('/')

app.run(debug=True)