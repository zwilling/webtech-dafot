<!DOCTYPE html>
<html lang="en" style="">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <title>DAFOT Assignment 4 Task 2 Reservation Acknowledgment</title>
    <meta name="description" content="">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/reservation.css">
    <script src="javascript/scripts.js"></script>
</head>
<body cz-shortcut-listen="true">

<!-- MAIN -->
<div role="main" id="main">
    <section class="reservation">
        <div class="container">
        <div class="headline">We reservated your seats.</div>
	<div class="headline">Please remember your reservation id:
	<!-- connect to SQL database and insert new reservation-->
	<?php
    	    //connect
    	    $db = new PDO('mysql:host=localhost;dbname=cinemareservation','root','');

    	    //insert reservation:
    	    //get variables from form
    	    $name = $_REQUEST['name'];
    	    $email = $_REQUEST['usermail']; 
    	    $cinema = $_REQUEST['cinema'];
	    $seats = $_REQUEST['seats'];
    
	    //determine reservation id
    	    $reservationId = rand(1000, 9999);


    	    // print($cinema);
    	    // print($name);
    	    // print($email);
    	    // print($reservationId);
    
	    //insert reservation into db
    	    $db->exec("INSERT INTO reservations
    	      (cinema, reservationid, email, name, seats) VALUES ('" . $cinema . "'," . $reservationId . ",'" . $email . "','" . $name . "','" . $seats . "')");

	    //print reservatioid for the user
	    print($reservationId);
	?>
	</div>
	<br>
    	<button id="back-button" class="pomegranate-flat-button" onclick="window.history.back()">Back to reservation</button>
	</div>
    </section>
</div>
<!-- ENDS MAIN -->

</body>
</html>
