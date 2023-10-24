import requests
import json
import time
from datetime import date
from flask import Flask, render_template

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=32.7157&longitude=-117.1647&current=temperature_2m,relativehumidity_2m,apparent_temperature,is_day,weathercode&temperature_unit=fahrenheit&timezone=America%2FLos_Angeles&forecast_days=1")
weather = response.json()
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('weatherapi.html', info=weather)

if __name__ == '__main__':
    app.run(debug=True)
