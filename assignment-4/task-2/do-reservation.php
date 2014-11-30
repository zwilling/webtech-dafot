<!DOCTYPE html>
<html lang="en" style="">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <title>DAFOT Assignment 4 Task 2 Reservation Acknowledgment</title>
    <meta name="description" content="">
    <link rel="stylesheet" href="css/style.css">
    <script src="javascript/scripts.js"></script>
</head>
<body cz-shortcut-listen="true">

<!-- connect to SQL database -->
<?php
    $verbindung = mysql_connect("localhost", "root","")
      or die ("Connection to MySQL not possible. Username or password wrong.");
    mysql_select_db("cinemareservation") 
      or die ("MySQL db does not exist.");
?>


<!-- HEADER -->
<header>
    <!-- header wrapper -->
    <div class="wrapper cf">
        <div id="logo">
            <a href="https://www3.elearning.rwth-aachen.de/ws14/14ws-14118/collaboration/Lists/WikiList1/Group%20DAFOT.aspx">
                <img src="./img/logo.png" alt="">
            </a>
        </div>
    </div>
    <!-- ENDS header wrapper -->
    <!-- nav -->
    <nav>
        <div>
            <ul id="nav" class="menu">
                <li><a href="https://www3.elearning.rwth-aachen.de/ws14/14ws-14118/Dashboard.aspx">WEB TECHNOLOGIES</a></li>
            </ul>
        </div>
    </nav>
    <!-- ends nav -->
</header>
<!-- ENDS HEADER -->

<!-- MAIN -->
<div role="main" id="main">
    <div class="wrapper">
        <!-- Reservation -->
        <section class="reservation">
            <div class="headline">Choose your seats</div>
                <div id="canvas-container" class="central-container">
                    <canvas id="can-reservation" width="600" height="400" class="dark-shadow">
                        <script>initReservationCanvas();</script>
                    </canvas>
                </div>
            <button id="buy-button" onclick="reserveSeats()" class="pomegranate-flat-button">Reserve seats</button>
        </section>
        <!-- ENDS Reservation -->
    </div>
</div>
<!-- ENDS MAIN -->
<footer>
    <!-- wrapper -->
    <div class="wrapper cf">
        <!-- social -->
        <div class="sb-holder cf">
            <ul id="social-bar" class="cf">
                <li class="left-corner"></li>
                <li><a href="http://www.facebook.com/" title="Become a fan"><img src="./img/Facebook.png"
                                                                                 alt="Facebook"></a></li>
                <li><a href="http://www.twitter.com/" title="Follow my tweets"><img src="./img/Twitter.png"
                                                                                    alt="twitter"></a></li>
                <li><a href="http://www.google.com/" title="Add to the circle"><img src="./img/Google+.png"
                                                                                    alt="Google plus"></a></li>
                <li class="right-corner"></li>
            </ul>
        </div>
        <!-- ENDS social -->
        <div id="footer-bottom">Assignment was made by <a href="#">DAFOT</a></div>
    </div>
    <!-- ENDS wrapper -->
</footer>
</body>
</html>
