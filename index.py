from datetime import datetime
from flask import Flask, render_template
fecha_actual = datetime.now()
dt_string = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main_page.html')

@app.route('/serial')
def serial():
    return render_template('arduino_serial.html')

@app.route('/credits')
def credits():
    return render_template('credits_page.html')

@app.route("/hey")
def heya():
    return "Entra <a href='/serial'><button>Entrar</button></a>"

if __name__ == '__main__':
    app.run(debug=True)
