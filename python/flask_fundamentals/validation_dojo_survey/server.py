from flask import Flask, render_template, request, flash, session, redirect
app = Flask(__name__)

app.secret_key = "this is a secret"

@app.route('/')
def index():
	return render_template('index.html', title="Dojo Survey")

@app.route('/result', methods=['POST'])
def result():
	results = {}
	error_count = 0
	for key, value in request.form.items():
		if len(value) < 1:
			error_count += 1
			flash(key + " too short")
		results[key] = value.capitalize()
	print len(request.form['comments']) > 120
	if len(request.form['comments']) > 120:
		error_count += 1
		flash("Comments too long, must be fewer than 120 characters")
	if error_count > 0:
		flash(str(error_count) + " errors")
		return redirect('/')
	return render_template('result.html', title="Survey Result", results=results)

app.run(debug=True)