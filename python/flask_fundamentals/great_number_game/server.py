from flask import Flask, session, redirect, render_template, request
app = Flask(__name__)

app.secret_key = "somesecretkey"

@app.route('/')
def index():
	return render_template('index.html', title="Great Number Game!")

@app.route('/guessed', methods=['POST'])
def guessed():
	session['guess'] = int(request.form['number'])
	guess = session['guess']
	
	import random
	try:
		current_num = session['current_num']
	except KeyError:
		session['current_num'] = random.randrange(1, 101)
		current_num = session['current_num']

	print request.form

	if(guess < current_num):
		result = 0
	elif(guess > current_num):
		result = 1
	elif(guess == current_num):
		result = 2
	session['result'] = result

	print session['result'], session['guess'], session['current_num'], "<------------------------------------"

	return redirect('/')

@app.route('/new-game', methods=['POST'])
def new_game():
	session.clear()
	return redirect('/')

app.run(debug=True)