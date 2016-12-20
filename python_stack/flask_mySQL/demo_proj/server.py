from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "SuchARagingClue"

mysql = MySQLConnector(app, 'superhero_demo')

@app.route('/')
def index():
	query = '''SELECT * FROM superheroes'''
	result = mysql.query_db(query)
	print result

	return render_template('index.html', title="Demo Home", result=result)

@app.route('/create', methods=['POST'])
def create():
	print request.form 
	data = {
		'first_name': request.form['first-name'],
		'last_name': request.form['last-name'],
		'hero_name': request.form['hero-name'],
	}
	query = """INSERT INTO superheroes (first_name, last_name, hero_name, created_at, updated_at) 
	VALUES (:first_name, :last_name, :hero_name, NOW(), NOW())"""

	print "here is what is coming back \n\n\n", mysql.query_db(query,data)
	return redirect('/')

@app.route('/hero/<id>')
def show(id):
	data = {'id': id}
	query = 'SELECT * FROM superheroes WHERE id = :id'
	hero = mysql.query_db(query, data)
	print hero
	return render_template('show.html', hero=hero[0])

@app.route('/update', methods=['POST'])
def update():
	print request.form
	return redirect('/')

app.run(debug=True)