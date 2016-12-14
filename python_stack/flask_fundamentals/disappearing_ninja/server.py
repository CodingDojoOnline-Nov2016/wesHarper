from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', title="Ninja Home")

@app.route('/ninjas/<ninja_color>')
def ninjas(ninja_color):
	print ninja_color
	print "<----------------------------------------------------------"
	print type(ninja_color)
	return render_template('ninjas.html', color=ninja_color, title=ninja_color + " ninja!")

app.run(debug=True)