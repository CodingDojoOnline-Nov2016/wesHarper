from flask import Flask, session, redirect, render_template, request, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "somesecret"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login_and_registrationdb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
	return render_template('index.html', title="Login and Registration")

@app.route('/users', methods=['POST'])
def create():
	first = request.form['first-name']
	last = request.form['last-name']
	email = request.form['email']
	password = request.form['password']
	confirm = request.form['confirm']
	errors = []

	if len(first) < 2:
		errors.append("First name must be at least 2 characters long")
	elif not first.isalpha():
		errors.append("First name must consist of only letters")

	if len(last) < 2:
		errors.append("Last name must be at least 2 characters long")
	elif not last.isalpha():
		errors.append("Last name must consist of only letters")

	if not EMAIL_REGEX.match(email):
		errors.append("Please enter a valid email address")

	if len(password) < 8:
		errors.append("Password must be at least 8 characters long")
	elif password != confirm:
		errors.append("Password and confirmation must match")

	if errors:
		for error in errors:
			flash(error)
		return redirect('/')
	else:
		pw_hash = bcrypt.generate_password_hash(password)
		query = '''INSERT INTO users(first_name, last_name, email, pw_hash, created_at, updated_at)
			VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())'''
		data = {
			'first_name': first,
			'last_name': last,
			'email': email,
			'pw_hash': pw_hash,
		}
		mysql.query_db(query, data)
		flash("Congrats buddy")
		return render_template('success.html', title="Success")


app.run(debug=True)