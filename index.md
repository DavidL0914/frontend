---
layout: nothing
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All in One</title>

  <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }

        /* Header styles */
        header {
            background-color: #333;
            color: #fff;
            padding: 10px;
            text-align: center;
        }

        header h1 {
            margin: 0;
        }

        /* Container for app sections */
        .app-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        /* Individual app sections */
  .app-section {
    flex: 1;
    min-width: 30%;
    margin: 10px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    overflow: hidden;
    padding: 10px; /* Add a slight padding to the div */
}

        .app-section img {
            width: 100%;
            height: auto;
        }

        /* Custom styling for specific sections */
        #weather {
            background-color: #DDF;
        }

        #todo {
            background-color: #EFE;
        }

        #recipe {
            background-color: #AED6F1;
        }

        #calendar {
            background-color: #F5F5DC;
        }

        #search {
            background-color: #FF8C88;
        }
    </style>
</head>

<body>
    <header>
        <h1>All in One</h1>
    </header>

  <div class="app-container">
        <div id="weather" class="app-section">
            <img src="WeatherAPI.png" alt="Weather">
        </div>
        <div id="todo" class="app-section">
            <img src="todo.png" alt="Todo List">
        </div>
        <div id="calendar" class="app-section">
            <img src="calendar.png" alt="Calendar">
        </div>
        <div id="recipe" class="app-section">
            <h2>Recipe of the Day</h2>
        </div>
        <div id="search" class="app-section">
            <h2>Search Bar for Recipe</h2>
        </div>
    </div>
</body>
</html>