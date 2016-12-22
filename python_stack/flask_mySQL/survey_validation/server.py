from flask import Flask, render_template, redirect, flash, request
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

name_regex = re.compile(r"^[a-zA-Z\-]+$")

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "SoSecret"
mysql = MySQLConnector(app, 'survey_validationdb')

@app.route('/')
def index():
	query = "SELECT * FROM users"
	students = mysql.query_db(query)
	return render_template('index.html', title="Survey Validation", students=students)

@app.route('/students', methods=['POST'])
def create():
	errors = []

	if len(request.form['first-name']) < 2:
		errors.append('First name must be at least 2 characters long')
	elif not name_regex.match(request.form['first-name']):
		errors.append('First name must not contain special characters or numbers')

	if len(request.form['last-name']) < 2:
		errors.append('Last name must be at least 2 characters long')
	elif not name_regex.match(request.form['last-name']):
		errors.append('Last name must not contain special characters or numbers')

	if len(request.form['password']) < 8:
		errors.append('Password must be at least 8 characters')
	elif request.form['password'] != request.form['confirm']:
		errors.append("Passwords don't match")

	if errors:
		for error in errors:
			flash(error)
	else:
		flash("nice job buddy")
		pw_hash = bcrypt.generate_password_hash(request.form['password'])
		data = {
			'first_name': request.form['first-name'],
			'last_name': request.form['last-name'],
			'password': pw_hash,
			'birth_date': request.form['birth-date'],
			'graduation_date': request.form['graduation-date'],
		}
		print data
		query = '''INSERT INTO users(first_name, last_name, password, birth_date, graduation_date, created_at, updated_at)
			VALUES (:first_name, :last_name, :password, :birth_date, :graduation_date, NOW(), NOW())'''
		mysql.query_db(query, data)
	print "made it again!"
	return redirect('/')

app.run(debug=True)