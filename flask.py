from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/meet')

def index():
	return render_template('home.html')

@app.route('/hello/')

def hello():

	return render_template('aboutme.html',z=a)

@app.route('/hi')

def hi():

	return render_template('contactme.html')

if __name__ == '__main__':
	app.debug = True
	app.run()
