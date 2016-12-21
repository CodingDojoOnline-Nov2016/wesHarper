from flask import Flask, redirect, render_template, request
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "ThisIsASecretKey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

mysql = MySQLConnector(app, 'full_friends')

@app.route('/')
def index():
	query = 'SELECT first_name, last_name, email FROM friends'
	friends = mysql.query_db(query)
	return render_template('index.html', title="Friends Home", friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	print request.form
	query = '''INSERT INTO friends(first_name, last_name, email, created_at, updated_at)
	VALUES (:first_name, :last_name, :email, NOW(), NOW())'''
	data = {
		'first_name': request.form['first-name'],
		'last_name': request.form['last-name'],
		'email': request.form['email'],
	}
	mysql.query_db(query, data)
	return redirect('/') 

app.run(debug=True)