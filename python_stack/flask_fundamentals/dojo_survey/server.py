from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', title="Dojo Survey")

@app.route('/result', methods=['POST'])
def result():
	results = {}
	for key, value in request.form.items():
		results[key] = value.capitalize()
	return render_template('result.html', title="Survey Result", results=results)

app.run(debug=True)