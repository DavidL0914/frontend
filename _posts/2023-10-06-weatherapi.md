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
  animation: animatedBackground 215s linear infinite;
  -webkit-animation: animatedBackground 215 s linear infinite;

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

    </style>
</head>
<body>
<div id="content">Partly Cloudy</div>
    <div class="weather-container"> 
        <div class="weather-info">
            <p><strong>Temperature:</strong> <span id="temperature"></span>°C</p>
            <p><strong>Humidity:</strong> <span id="humidity"></span>%</p>
            <p><strong>Time:</strong> <span id="time"></span></p>
            <p><strong>Day:</strong> <span id="day"></span></p>
        </div>
    </div>

    <script>
        // JavaScript code to fetch and display weather data
        async function fetchWeather() {
            try {
                const response = await fetch('https://api.weatherapi.com/v1/current.json?key=03557ba66442468e94e161533230910&q=San%20Diego');
                const data = await response.json();
                const temperatureElement = document.getElementById('temperature');
                const humidityElement = document.getElementById('humidity');
                const timeElement = document.getElementById('time');
                const dayElement = document.getElementById('day');

                temperatureElement.textContent = data.current.temp_c;
                humidityElement.textContent = data.current.humidity;
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
