<!DOCTYPE html>
<html lang="en" style="">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <title>DAFOT Assignment 4 Task 2 Reservation</title>
    <meta name="description" content="">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/reservation.css">
    <script src="javascript/scripts.js"></script>
</head>
<body cz-shortcut-listen="true">
<!-- MAIN -->
    <div role="main" id="main" >
        <div class="container">
        <!-- Reservation -->
        <div class="headline">Choose your seats</div>
            <section class="reservation">
	        <?php
		    //connect to database
		    $db = new PDO('mysql:host=localhost;dbname=cinemareservation','root','');

		    //get reservated seats and add them to js
		    $query = "SELECT * FROM reservations";
		    $result = $db->query($query);
		    if($result){
		        foreach($result as $row){
		            print($row['cinema']);
		            //TODO: add seats to javascript
		        }
		    }
		    else{
		        print("No current reservations found");
		    }
		?>
                    <div id="canvas-container" class="central-container">
                        <canvas id="can-reservation" width="520" height="400" class="dark-shadow">
                            <script>initReservationCanvas();</script>
                        </canvas>
                    </div>
            </section>
            <!-- ENDS Reservation -->
            <!-- Contacts -->
            <section class="contacts">
                <!-- <div class="headline">Please enter your contact details</div> -->
                <form name="contacts" action="do-reservation.php" accept-charset="utf-8">
                    <div class="feature">
                        <fieldset class="fields">
                            <div class="form-group">
                                <label for="name">Name :</label>  
                                <input type="text" name="name" placeholder="Peter Mustermann" size="20" required>
                            </div>
                            <div class="form-group">
                                <label for="usermail">Email :</label>  
                                <input type="email" name="usermail" placeholder="example@email.com" size="20" required>
                            </div>
                        </fieldset>
                    </div>
                    <input type="submit" id="submit-form" class="pomegranate-flat-button" value="Confirm">
                </form>
		<script>
		  //add cinema as hidden field to the form
		  var cinemaInput = document.createElement('input');
		  cinemaInput.type = 'hidden';
		  cinemaInput.name = 'cinema';
		  cinemaInput.value = selectedCinema;
		  document.forms["contacts"].appendChild(cinemaInput);
		</script>
            </section>
            <!-- ENDS Contacts -->
        </div>
    </div>
</body>
</html>