from flask import Flask, flash, redirect, render_template, session, request
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'SuchAClue'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

mysql = MySQLConnector(app, 'emailvalidationdb')

@app.route('/')
def index():
	return render_template('index.html', title="Email Validation Home")

@app.route('/success')
def success():
	flash("Successfully added email", 'success')
	query = "SELECT * FROM emails"
	emails = mysql.query_db(query)
	return render_template('success.html', title="Email List", emails=emails)

@app.route('/add_email', methods=['POST'])
def add_email():
	if not EMAIL_REGEX.match(request.form['email']):
		flash('please enter a valid email address', 'errors')
		return redirect('/')
	else:
		query = """INSERT INTO emails (email, created_at, updated_at)
		VALUES (:email, NOW(), NOW())"""
		data = {
			'email': request.form['email'],
		}
		mysql.query_db(query, data)
		return redirect('/success')

@app.route('/delete/<id>')
def delete_email(id):
	query = "DELETE FROM emails WHERE id = :id"
	data = {'id': id,}
	print mysql.query_db(query,data)
	return redirect('/success')
app.run(debug=True)