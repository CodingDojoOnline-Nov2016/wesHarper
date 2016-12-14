from flask import Flask, session, render_template, redirect

app = Flask(__name__)

app.secret_key = "this is secret"

@app.route('/')
def index():
	try:
		session['counter'] += 1
	except KeyError:
		session['counter'] = 1
	return render_template('index.html', title="Counter Home")

@app.route('/reset')
def reset():
	session['counter'] = 0
	return redirect('/')

@app.route('/add2')
def add2():
	session['counter'] += 1
	return redirect('/')

app.run(debug=True)