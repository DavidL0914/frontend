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

</style>
</head>

<body>
    <div class="weather-container">
        <h1>San Diego Weather</h1>
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
                const response = await fetch('https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=San%20Diego');
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