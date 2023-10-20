import requests
import json
import time
from datetime import date
from flask import Flask, render_template

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=33.014252&longitude=-117.121288&hourly=temperature_2m,relativehumidity_2m,precipitation_probability,weathercode&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset&temperature_unit=fahrenheit&timezone=America%2FLos_Angeles")
#print(response.status_code)
#print(response.json())
weather = response.json()
#print(weather)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
daynumbers = []
for i in range(31):
    daynumbers.append(str(i))

def datemaker(date):
    year = date[0:4:1]
    #print(year)
    month = date[5:7:1]
    month = months[int(month)-1]
    #print(month)
    day = date[8:10:1]
    #print(day)
    return f"{month} {day}, {year}"
    
    
datestemp = []
dates = []
for x in weather["daily"]["time"]:
    datestemp.append(x)
for i in range(len(datestemp)):
    dates.append(datemaker(datestemp[i]))

def printweather(weather, dates):
    counter = 0
    global temps
    temps = []
    precipitation = []
    for x in weather["hourly"]["temperature_2m"]:
        temps.append(x)
    for x in weather["hourly"]["precipitation_probability"]:
        precipitation.append(x)
    print(dates)
    print(temps)
    print(precipitation)
    for i in range(7):
        print("Date:",dates[i])
        for i in range(24):
            print(f"The temperature at {i} o'clock is {temps[counter]} degrees.")
            print(f"The chance of precipitation at {i} o'clock is {precipitation[counter]}%\n")
            counter += 1

#printweather(weather, dates)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', temps=weather["hourly"]["temperature_2m"])

if __name__ == '__main__':
    app.run(debug=True)
