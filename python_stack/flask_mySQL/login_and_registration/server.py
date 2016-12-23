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

@app.route('/users/<id>/profile')
def users(id):
	query = """SELECT first_name, last_name FROM users
		WHERE id = :id"""
	data = { 'id': id }
	user = mysql.query_db(query, data)
	return render_template('success.html', title="Success!", user=user)

@app.route('/users', methods=['POST'])
def create():
	first = request.form['first-name']
	last = request.form['last-name']
	email = request.form['email']
	password = request.form['password']
	confirm = request.form['confirm']
	errors = []

	#check to see if email address exists in system
	validation_query = "SELECT id FROM users WHERE email= :email"
	validation_data = { 'email': email }
	user_check = mysql.query_db(validation_query, validation_data)
	if user_check:
		errors.append("A user exists with that email, please login or register with a different account")

	#validation checks
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

	#handle errors
	if errors:
		for error in errors:
			flash(error)
		return redirect('/')
	else:
		#store new user in db
		pw_hash = bcrypt.generate_password_hash(password)
		insert_query = '''INSERT INTO users(first_name, last_name, email, pw_hash, created_at, updated_at)
			VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())'''
		insert_data = {
			'first_name': first,
			'last_name': last,
			'email': email,
			'pw_hash': pw_hash,
		}
		mysql.query_db(insert_query, insert_data)

		#pull user_id for routing
		user_query = "SELECT id FROM users WHERE email = :email LIMIT 1"
		user_data = { 'email': email }
		user = mysql.query_db(user_query, user_data)
		flash("successful registration")
		session['user_id'] = user[0]['id']
		return redirect('/users/'+str(session['user_id'])+'/profile')

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	if email and password:
		user_query = "SELECT id, email, pw_hash FROM users WHERE email = :email LIMIT 1"
		query_data = { 'email': email }
		try:
			user = mysql.query_db(user_query, query_data)
			if bcrypt.check_password_hash(user[0]['pw_hash'], password):
				session['user_id'] = user[0]['id']
				flash('successful login')
				return redirect('/users/'+str(session['user_id'])+'/profile')
			else:
				flash('incorrect password')
				return redirect('/')
		except:
			flash('no user exists with that email')
			return redirect('/')
	else:
		flash('unsuccessful login')
		return redirect('/')

@app.route('/users/<id>/delete', methods=['POST'])
def destroy(id):
	query = "DELETE FROM users WHERE id= :id"
	data = { 'id': id }
	mysql.query_db(query, data)
	session['user_id'] = None
	return redirect('/')

app.run(debug=True)