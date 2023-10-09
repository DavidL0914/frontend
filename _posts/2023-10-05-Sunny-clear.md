---
toc: true
comments: true
layout: 
title: Sunny Clear Test
description: Frontend page for Sunny Clear Weather
type: plans
courses: { csse: {week: 1}, csp: {week: 1, categories: [4.A]}, csa: {week: 0} }
---

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

<div id="content">Partly Cloudy</div>

