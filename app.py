import requests
import json
import time
from datetime import date
from flask import Flask, render_template

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=32.7157&longitude=-117.1647&hourly=temperature_2m,relativehumidity_2m,precipitation_probability,weathercode&temperature_unit=fahrenheit&timezone=America%2FLos_Angeles&forecast_days=1")
weather = response.json()
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('weathertesting.html', info=weather)

if __name__ == '__main__':
    app.run(debug=True)
