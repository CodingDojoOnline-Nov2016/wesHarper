from flask import Flask, redirect, request, session, flash, render_template
import re, datetime

email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
name_regex = re.compile(r'[a-zA-Z]')
password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d$@$!%*?&]{8,}')

app = Flask(__name__)
app.secret_key = "SuchARagingClue"

@app.route('/')
def index():
	return render_template('index.html', title="Registration Form")

@app.route('/process', methods=['POST'])
def process_form():
	error_count = 0
	for key, value in request.form.items():
		if len(value) < 1:
			flash(u'Invalid ' + key + ', all fields required', 'error')
			error_count += 1
	if not name_regex.match(request.form['first-name']):
		flash(u'Invalid First Name, must contain only letters', 'error')
		error_count += 1
	if not name_regex.match(request.form['last-name']):
		flash(u'Invalid Last Name, must contain only letters', 'error')
		error_count += 1
	if not email_regex.match(request.form['email']):
		flash(u'Invalid email', 'error')
		error_count += 1
	if len(request.form['password']) < 8:
		flash(u'Password must be at least 8 characters', 'error')
		error_count += 1
	if not password_regex.match(request.form['password']):
		flash(u'Password must contain at least one capital letter and one number', 'error')
		error_count += 1
	if request.form['password'] != request.form['confirm']:
		flash(u"Passwords don't match", 'error')
		error_count += 1
	try:
		datetime.datetime.strptime(request.form['birthdate'], '%m/%d/%Y')
	except ValueError:
		flash(u"Must be a valid date in MM/DD/YYYY format", 'error')
		error_count += 1
	if error_count > 0:
		flash(u"Please fix your " + str(error_count) + " errors.", 'error')
	else:
		flash(u"Thanks for submitting your information", 'congrats')
	return redirect('/')

app.run(debug=True)