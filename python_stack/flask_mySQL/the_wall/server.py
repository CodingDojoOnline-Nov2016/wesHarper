from flask import Flask, session, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
from datetime import datetime
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "SuchARagingClue"
mysql = MySQLConnector(app, 'the_walldb')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/') #Render home page(wall)
def index():
	#query messages
	message_query = """SELECT messages.id AS message_id,
		messages.message AS message, 
		messages.created_at AS message_date,
		messages.id AS message_id,
		users.first_name AS creator_first_name,
		users.last_name AS creator_last_name FROM messages
			JOIN users ON messages.users_id = users.id
			ORDER BY messages.created_at DESC"""
	messages = mysql.query_db(message_query)

	#query comments
	comment_query = """SELECT comments.id AS comment_id,
		comments.comment AS comment,
		comments.created_at AS comment_date,
		messages.id AS message_id,
		users.first_name AS creator_first_name,
		users.last_name AS creator_last_name FROM comments
			JOIN users ON comments.users_id = users.id
			JOIN messages ON comments.messages_id = messages.id
			ORDER BY comments.created_at ASC"""
	comments = mysql.query_db(comment_query)

	#check if user is logged in and pull info
	if not session['logged_in'] and not session['user_id']:
		return render_template('index.html', title="The Wall", messages=messages, comments=comments)
	elif not session['logged_in']:#there are cases in which user will be logged out but user_id still extists in session
		user_query = "SELECT first_name, last_name, email FROM users WHERE id = :id"
		user_data = { 'id': session['user_id'] }
		user = mysql.query_db(user_query, user_data)
		return render_template('index.html', title="The Wall", user=user, messages=messages, comments=comments)
	else:
		user_query = "SELECT first_name, last_name FROM users WHERE id = :id"
		user_data = { 'id': session['user_id'] }
		user = mysql.query_db(user_query, user_data)		
		return render_template('index.html', title=str(user[0]['first_name'])+" "+str(user[0]['last_name']), user=user, messages=messages, comments=comments)

@app.route('/register') #Render registration page
def register():
	return render_template('register.html', title="Sign Up")

@app.route('/users', methods=['POST']) #Create a new user
def create_user():
	print request.form
	first = request.form['first-name']
	last = request.form['last-name']
	email = request.form['email']
	password = request.form['password']
	confirm = request.form['confirm']

	#create empty error list for error handling
	errors = []

	#check for duplicate users
	duplicate_query = "SELECT email FROM users WHERE email = :email"
	duplicate_data = { 'email': email }
	duplicate_check = mysql.query_db(duplicate_query, duplicate_data)
	if duplicate_check:
		errors.append("User exists with that email, sign up with a new account or login")

	#run form validations
	if len(first) < 1:
		errors.append("Please enter a first name")
	elif not first.isalpha():
		errors.append("First name must contain only letters")

	if len(last) < 1:
		errors.append("Please enter a last name")
	elif not last.isalpha():
		errors.append("Last name must contain only letters")

	if not EMAIL_REGEX.match(email):
		errors.append("Please enter a valid email address")

	if len(password) < 8:
		errors.append("Your password must be at least 8 characters")
	elif password != confirm:
		errors.append("Passwords don't match")

	if errors:
		for error in errors:
			flash(error)
			return redirect('/register')
	else:
		#create pw_hash
		pw_hash = bcrypt.generate_password_hash(password)

		#run insert query
		insert_query = """INSERT INTO users(first_name, last_name, email, pw_hash, created_at, updated_at)
			VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"""
		insert_data = {
			'first_name': first,
			'last_name': last,
			'email': email,
			'pw_hash': pw_hash,
		}
		mysql.query_db(insert_query, insert_data)

		#query for user_id
		query = "SELECT id FROM users WHERE email = :email"
		data = { 'email': email }
		user = mysql.query_db(query, data)

		#set user_id to queried id and prep for dynamic content and login
		session['user_id'] = user[0]['id']
		session['logged_in'] = True
	return redirect('/')

@app.route('/login', methods=['POST'])#log user in
def login():
	print request.form
	email = request.form['email']
	password = request.form['password']

	#run login query
	query = "SELECT id, pw_hash FROM users WHERE email = :email"
	data = { 'email': email }
	user = mysql.query_db(query, data)

	#check password
	if bcrypt.check_password_hash(user[0]['pw_hash'], password):
		session['logged_in'] = True
		session['user_id'] = user[0]['id']
	else:
		flash("incorrect username or password")
	return redirect('/')

@app.route('/logout')#log user out
def logout():
	session['logged_in'] = False
	print "*"* 50
	print session['logged_in']
	return redirect('/')

@app.route('/messages', methods=['POST'])#create a new message
def create_message():
	#create error handler
	message = request.form['message']
	errors = []
	#check if user is logged in before allowing post into db
	if not session['logged_in']:
		errors.append('must be logged in to create messages')

	#run length validation
	if len(message) < 15:
		errors.append("message must be longer than 15 characters")

	#check for errors
	if errors:
		for error in errors:
			flash(error)
		return redirect('/')
	else:
		#run insert query
		query = """INSERT INTO messages(message, created_at, updated_at, users_id)
			VALUES (:message, NOW(), NOW(), :users_id)"""
		data = {
			'message': message,
			'users_id': session['user_id']
		}
		mysql.query_db(query, data)
	return redirect('/')

@app.route('/comments', methods=['POST'])
def create_comment():
	messages_id = request.form['message-id']
	comment = request.form['comment']
	#create error handler
	errors = []
	#check if user is logged in before allowing to add comment
	if not session['logged_in']:
		errors.append('must be logged in to comment')

	#run length validation
	if len(comment) < 1:
		errors.append("comment cannot be blank")

	#check for errors
	if errors:
		for error in errors:
			flash(error)
		print errors
		print "*"* 50
		return redirect('/')
	else:
		#run insert query
		query = """INSERT INTO comments(comment, created_at, updated_at, users_id, messages_id)
			VALUES (:comment, NOW(), NOW(), :users_id, :messages_id)"""
		data = {
			'comment': comment,
			'users_id': session['user_id'],
			'messages_id': messages_id,
		}
		mysql.query_db(query, data)
	return redirect('/')

app.run(debug=True)