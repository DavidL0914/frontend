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
    <title>Weather</title>

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
  to { background-p osition: 100% 100%; }
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

.contain {
  position: fixed;
  top: 15%;
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
  top: 80%;
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

.big {
  font-size: 3vw;
}

.enter-city {
  position: fixed;
  top: 65%;
  left: 45%;
  transform: translate(-50%, -50%);
}

.input-box {
  position: fixed;
  top: 65%;
  left: 55%;
  transform: translate(-50%, -50%);
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

<div>
    <label for="userInput">Enter a City: </label>
    <input type="text" id="userInput">
    <button onclick="updateWeather()">Get Weather</button>
</div>

<div class="contain">
    <h1 class="big" id="city"></h1>
</div>
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

<script>

const weatherBackgrounds = {
  'Clear': 'url(link_to_sunny_image)',
  'Partly cloudy': 'url(link_to_partly_cloudy_image)',
  'Cloudy': 'url(link_to_cloudy_image)',
  'Rain': 'url(link_to_rainy_image)',
  // Add more conditions and corresponding image URLs as needed
};

async function updateWeather() {
    const userInput = document.getElementById("userInput").value;
    // Replace spaces with "%20" to ensure proper URL formatting
    const city = userInput.replace(/ /g, "%20");
    const apiUrl = `https://api.weatherapi.com/v1/current.json?key=03557ba66442468e94e161533230910&q=${city}`;

    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        const temperatureElement = document.getElementById('temperature');
        const humidityElement = document.getElementById('humidity');
        const timeElement = document.getElementById('time');
        const dayElement = document.getElementById('day');
        const weathertypeElement = document.getElementById('title');
        const citynameElement = document.getElementById('city');

        temperatureElement.textContent = data.current.temp_c;
        humidityElement.textContent = data.current.humidity;
        weathertypeElement.textContent = data.current.condition.text;
        citynameElement.textContent = data.location.name;

        const currentTime = new Date();
        timeElement.textContent = currentTime.toLocaleTimeString();
        dayElement.textContent = currentTime.toLocaleDateString();
    } catch (error) {
        console.error('Error fetching weather data:', error);
    }
}


updateWeather(); // Initial call to load weather data

setInterval(function () {
    updateWeather();
}, 1000);

</script>
</body>
</html>