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

/*CSS For Calendar*/
  button {
    width: 75px;
    cursor: pointer;
    box-shadow: 0px 0px 2px gray;
    border: none;
    outline: none;
    padding: 5px;
    border-radius: 5px;
    color: white;
  }
  
  #header {
    padding: 10px;
    color: #d36c6c;
    font-size: 26px;
    font-family: sans-serif;
    display: flex;
    justify-content: space-between;
  }
  #header button {
    background-color:#92a1d1;
  }
  #container {
    width: 770px;
  }
  #weekdays {
    width: 100%;
    display: flex;
    color: #247BA0;
  }
  #weekdays div {
    width: 100px;
    padding: 10px;
  }
  #calendar {
    width: 100%;
    margin: auto;
    display: flex;
    flex-wrap: wrap;
  }
  .day {
    width: 100px;
    padding: 10px;
    height: 100px;
    cursor: pointer;
    box-sizing: border-box;
    background-color: white;
    margin: 5px;
    box-shadow: 0px 0px 3px #CBD4C2;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .day:hover {
    background-color: #e8faed;
  }
  
  .day + #currentDay {
    background-color:#e8f4fa;
  }
  .event {
    font-size: 10px;
    padding: 3px;
    background-color: #58bae4;
    color: white;
    border-radius: 5px;
    max-height: 55px;
    overflow: hidden;
  }
  .padding {
    cursor: default !important;
    background-color: #FFFCFF !important;
    box-shadow: none !important;
  }
  #newEventModal, #deleteEventModal {
    display: none;
    z-index: 20;
    padding: 25px;
    background-color: #e8f4fa;
    box-shadow: 0px 0px 3px black;
    border-radius: 5px;
    width: 350px;
    top: 100px;
    left: calc(50% - 175px);
    position: absolute;
    font-family: sans-serif;
  }
  #eventTitleInput {
    padding: 10px;
    width: 100%;
    box-sizing: border-box;
    margin-bottom: 25px;
    border-radius: 3px;
    outline: none;
    border: none;
    box-shadow: 0px 0px 3px gray;
  }
  #eventTitleInput.error {
    border: 2px solid red;
  }
  #cancelButton, #deleteButton {
    background-color: #d36c6c;
  }
  #saveButton, #closeButton {
    background-color: #92a1d1;
  }
  #eventText {
    font-size: 14px;
  }
  #modalBackDrop {
    display: none;
    top: 0px;
    left: 0px;
    z-index: 10;
    width: 100vw;
    height: 100vh;
    position: absolute;
    background-color: rgba(0,0,0,0.8);
  }
</style>
</head>

<body>
    <div id = "weather" >Weather</div>
    <div id = "todo">Todo</div>
    <div id = "calendar">Calendar</div>
    <div id = "recipe" >Recipe of the Day</div>
    <div id = "search" >Search Bar for Recipe</div>
</body>
</html>