from datetime import datetime
from flask import Flask, render_template, request
from dttime import dt


app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    return render_template('main_page.html', hora=str(dt))

@app.route('/serial')
def serial():
    return render_template('arduino_serial.html')

@app.route('/credits')
def credits():
    return render_template('credits_page.html')

@app.route("/hey")
def heya():
    return "owo"

#@app.route("/<usr>")
#def user(usr):
#    return f"<h1>Hello {usr} | </h1>"

##Entra <a href='/serial'><button>Entrar</button></a>
if __name__ == '__main__':
    app.run(debug=True)
