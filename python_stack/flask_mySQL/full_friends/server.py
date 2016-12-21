from flask import Flask, redirect, render_template, request, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "ThisIsASecretKey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

mysql = MySQLConnector(app, 'full_friends')

@app.route('/')
def index():
	query = 'SELECT first_name, last_name, email, id FROM friends'
	friends = mysql.query_db(query)
	return render_template('index.html', title="Friends Home", friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	error_count = 0
	if not EMAIL_REGEX.match(request.form['email']):
		flash('please enter a valid email address')
		error_count += 1
	if not NAME_REGEX.match(request.form['first-name']):
		flash('please enter a valid first name')
		error_count += 1
	if not NAME_REGEX.match(request.form['last-name']):
		flash('please enter a valid last name')
		error_count += 1
	if error_count == 0:
		query = '''INSERT INTO friends(first_name, last_name, email, created_at, updated_at)
		VALUES (:first_name, :last_name, :email, NOW(), NOW())'''
		data = {
			'first_name': request.form['first-name'],
			'last_name': request.form['last-name'],
			'email': request.form['email'],
		}
		mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	query = '''SELECT first_name, last_name, email, id FROM friends
	WHERE id = :id'''
	data = {
		'id': id,
	}
	friend = mysql.query_db(query, data)
	return render_template('edit.html', title="Edit Friend", friend=friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	error_count = 0
	if not EMAIL_REGEX.match(request.form['email']):
		flash('please enter a valid email address')
		error_count += 1
	if not NAME_REGEX.match(request.form['first-name']):
		flash('please enter a valid first name')
		error_count += 1
	if not NAME_REGEX.match(request.form['last-name']):
		flash('please enter a valid last name')
		error_count += 1
	if error_count == 0:
		print id
		query = '''UPDATE friends
		SET first_name = :first_name, 
			last_name = :last_name,
			email = :email,
			updated_at = NOW()
			WHERE id = :id'''
		data = {
			'first_name': request.form['first-name'],
			'last_name': request.form['last-name'],
			'email': request.form['email'],
			'id': id,
		}
		mysql.query_db(query, data)
		return redirect('/')
	return redirect('/friends/'+id+'/edit')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
	query = '''DELETE FROM friends WHERE id = :id'''
	data = { 'id': id }
	mysql.query_db(query, data)
	return redirect('/')

app.run(debug=True)