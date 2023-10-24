---
layout: nothing
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Layout Page</title>

<style>
div#weather {
    background-color: #DDF;
    height: 35%;
    width: 70%;
    margin-left: 1%;
    margin-top: 1%;
}

div#todo {
    background-color: green;
    height: 45%;
    width: 26%;
    position: absolute;
    left: 72%;
    top: 1%;
}

div#recipe {
    background-color: blue;
    height: 30%;
    width: 45%;
    position: absolute;
    left: 53%;
    top: 50%;
}

div#calendar {
    background-color: #0FF;
    width: 50%;
    position: absolute;
    top: 38%;
    min-height: 61%;
    margin-left: 1%;
}

div#search {
    background-color: red;
    width: 20%;
    position: absolute;
    top: 83%;
    min-height: 12%;
    left: 67%;
}

.todo img {
    object-fit: contain;
}
</style>
</head>

<body>
    <div id = "weather" >Weather</div>
    <div id = "todo">Todo</div>
    <div id = "calendar" >Calendar</div>
    <div id = "recipe" >Recipe of the Day</div>
    <div id = "search" >Search Bar for Recipe</div>
</body>
</html>
