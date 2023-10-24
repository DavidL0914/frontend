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
    <div id = "todo" >
    <img src="https://ci3.googleusercontent.com/mail-img-att/AM67uINCukI8cSJmWrS-URb_XDwNNXFuBUAOIdSmINFlpNxy7Yf5B4Yy1g9knAxY9pD5N0RpOdXrF461tOGuwdMtBC-d3PuCltTFVsTsuVVF3YQGtKMVuDA9KjsOuXh2nSw-CXI1vpgMiXBsBfP9wTh9S3k1zBX8BHjIJeG1Hw4PdGAuktvpCZ6GmhN2UvEENljYOpPOqis1Q40Tz5Vb5Tpby-Qe_ElDnJLg8lXl17LUU_IihbT8sn3-gMnJSxJ9g7JbO1n7G1hLYuBK5xp5NVHqy8TNOsmtHyfoFwntxhjxOATBUrMeEd4Hg0V_PN2bDCRCBc3mbn1besSzV6aABcDgNK-uAHwmJpsOx0s4Bm7vgGNu_O9yHSDkD7PZyf7JFfomyG0ty-rHPjjEN-FG4YdoVw4a5yhuSkCqLFYdSMXaJoAh7ZhSK2nW-R_J5XGwRRO4NcAgQF56DTGVJEsU1qz8CSKTPE-hv6jo1pwGPju_v85bQ2wLVCc72vJBQKXDNkYbd2ZzE-wtZxL_9-DgabvD0yDiSFFnXEmOvtl4WpwF9qTb36tYQcjtY-azTMrrsbjlI2KHvy7vNWBUe8MqkPjfAWPfdInUrpHxQxsjCuK3nI-ypTUHxq4N7VAApOYtdoq2CouxRzU1HSNgZ92chqIFbpMHAWmRZcCpxmaMqoCyi6bkRWPPIpo3cbGtK7ZOD1WdrG7mY0ffditta9mJcnk27dNYDCHAhKnmwHB1ZdQaHr1CSX0rbIat5aOuR7oyL4rKr3qK8YEdo1-OJ9M46x-oNT4IZMF340IyJfq_6AhCu75d5INqKM1sxbczqUtzLv0oFtXCRoNpI4Dup9W4wvAKA36SyDEsyfRWvNTE_6EqYS0DSg_TM7s9whTCnIBeRVL0i8Qhyj9iLddETQ6k_mxLJ6bzcvxquLebCDIH1IUYGvJKsxgVRvYLRvaMdYnmURJUnzd2Kk8KKOv6v9FR7-6KQ_Im7OZl4HMjt3fA3IvUQ5Bcr71__34nUz1LmEfH-Y60JaxKkJ9WXWMvAGG07hNvDkeQudSJHt7B1f79IVCj3VFSgbQ6OA_n4o8=s0-l75-ft">
    </div>
    <div id = "calendar" >Calendar</div>
    <div id = "recipe" >Recipe of the Day</div>
    <div id = "search" >Search Bar for Recipe</div>
</body>
</html>
