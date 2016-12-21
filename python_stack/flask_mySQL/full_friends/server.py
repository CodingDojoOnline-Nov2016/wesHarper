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
	print friends
	return render_template('index.html', title="Friends Home", friends=friends)

app.run(debug=True)