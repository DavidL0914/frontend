---
toc: true
comments: true
layout: 
title: API Test
description: Weather API Test
type: plans
courses: { csse: {week: 1}, csp: {week: 1, categories: [4.A]}, csa: {week: 0} }
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>San Diego Weather</title>

<style>

body {
  width: 100%; 
  height:100%;
  margin:0em 0%;
  background-color:#8ec1da;
  background-image: url("https://static.vecteezy.com/system/resources/previews/002/968/352/original/panorama-sky-with-cloud-on-a-sunny-day-free-photo.jpg");
  background-position: center bottom;
  animation: animatedBackground 500s linear infinite;
  -webkit-animation: animatedBackground 500 s linear infinite;

}
@keyframes animatedBackground {
  from { background-position: 0 100%; }
  to { background-position: 100% 100%; }
}
@-webkit-keyframes  animatedBackground {
  from { background-position: 0 100%; }
  to { background-position: 100% 100%; }
}

#content {
  position:fixed;
  top:4vw;
  height:1em;
  width:100vw;
  color:white;
  text-align: center;
  font-size: 3.5vw;
}

.title {
  position: fixed;
  top: 25%;
  left: 50%;
  transform: translate(-50%, -50%);
}

/* Styles for the transparent gray box */
.transparent-box1 {
  position: fixed;
  top: 50%;
  left: 25%;
  transform: translate(-50%, -50%);
  background-color: rgba(128, 128, 128, 0.5); /* Transparent gray color */
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.transparent-box2 {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: rgba(128, 128, 128, 0.5); /* Transparent gray color */
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.transparent-box3 {
  position: fixed;
  top: 50%;
  left: 75%;
  transform: translate(-50%, -50%);
  background-color: rgba(128, 128, 128, 0.5); /* Transparent gray color */
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.get-weather {
  position: fixed;
  top: 70%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: rgba(38, 152, 255, 0.5);
  border: none;
  width: 10%;
  height: 12%;
  border-radius: 10px;
}

.get-weather:hover {
    background-color: rgba(82, 169, 255, 0.5)
}

/* Add some basic styling to the navigation bar */
ul.navbar {
    list-style-type: none;
    margin: 0;
    padding: 0;
    background-color: #333;
    overflow: hidden;
    opacity: 0.5;
}

/* Style the navigation bar items */
ul.navbar li {
    float: left;
}

/* Style the links within the navigation bar */
ul.navbar li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

/* Change the link color on hover */
ul.navbar li a:hover {
    background-color: #555;
}

</style>
</head>

<body>
<ul class="navbar">
    <li><a href="#home">Weather</a></li>
    <li><a href="#about">Calendar</a></li>
    <li><a href="#services">To-do List</a></li>
    <li><a href="#contact">Logout</a></li>
</ul>
<!--
<div>
    <label for="userInput">Enter City: </label>
    <input type="text" id="userInput">
    <button onclick="displayInput()">Submit</button>
</div>
<div id="content">Partly Cloudy</div>
-->
  <div class="title">
    <h1 id="title"></h1>
  </div>
  <div class="transparent-box1">
    <p><strong>Temperature:</strong> <span id="temperature"></span>°C</p>
  </div>

  <div class="transparent-box2">
    <p><strong>Humidity:</strong> <span id="humidity"></span>%</p>
  </div>

  <div class="transparent-box3">
    <p><strong>Time:</strong> <span id="time"></span></p>
            <p><strong>Day:</strong> <span id="day"></span></p>
  </div>
  <div>
    <button class="get-weather" onclick="fetchWeather()">Get Weather</button>
  </div>

<script>
        // JavaScript code to fetch and display weather data
        //async function displayInput() {
            //var userInput = document.getElementById("userInput").value;
            //console.log(userInput)
            //var temp = userInput.innerHTML;
            //console.log(typeof temp)
            //console.log(temp)
            // var city = temp.replace(" ", "%20")
        //}
        //displayInput();
        async function fetchWeather() {
            try {
                var link
                const response = await fetch('https://api.weatherapi.com/v1/current.json?key=03557ba66442468e94e161533230910&q=san%20diego');
                const data = await response.json();
                const temperatureElement = document.getElementById('temperature');
                const humidityElement = document.getElementById('humidity');
                const timeElement = document.getElementById('time');
                const dayElement = document.getElementById('day');
                const weathertypeElement = document.getElementById('title')
                temperatureElement.textContent = data.current.temp_c;
                humidityElement.textContent = data.current.humidity;
                weathertypeElement.textContent = data.current.condition.text;
                console.log(data)
                console.log(data.current)
                console.log(data.current.condition.text)
                const currentTime = new Date();
                timeElement.textContent = currentTime.toLocaleTimeString();
                dayElement.textContent = currentTime.toLocaleDateString();
            } catch (error) {
                console.error('Error fetching weather data:', error);
            }
        }
        fetchWeather();
</script>
</body>
</html>
