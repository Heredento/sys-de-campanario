from datetime import datetime
from flask import Flask, render_template, request
from dttime import dt
#import config

app = Flask(__name__)

@app.route("/register")
def register():
    return render_template('registro.html')

@app.route("/login")
def login():
    return render_template('login.html')



@app.route('/', methods=["POST", "GET"])
def home():
    return render_template('events.html', hora=str(dt))

@app.route('/admin')
def serial():
    return render_template('admin.html')

@app.route('/credits')
def credits():
    return render_template('credits.html')

if __name__ == '__main__':
    app.run(debug=True)
