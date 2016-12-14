from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', title='Home of "Ninjas"')

@app.route('/ninjas')
def ninjas():
	return render_template('ninjas.html', title='Ninjas')

@app.route('/dojos/new')
def dojos():
	return render_template('dojos.html', title='Dojos')

app.run(debug=True)