We used XAMPP for this task. Here are the steps to setup the site:

1. Install XAMPP
2. Checkout your solution
3. Start XAMPP
4. Setup MySQL:
     open localhost in your browser
     go to PhpMyAdmin
     create new db (on the left)
     name the db cinemareservation and accept
     select the db on the left and go to the SQL tab
     initialize the tables with the following SQL command:	
       	CREATE TABLE reservations (id int NOT NULL,
	  cinema varchar(150),
	  reservationid int,
	  email varchar(150),
	  name varchar(150),
	  seats varchar(2000));
	INSERT INTO reservations VALUES (1, 'IMAX', 1111, 'already@booked.de', 'Someone', '[{"row":9,"column":4,"free":true,"inReservation":true},{"row":9,"column":5,"free":true,"inReservation":true},{"row":9,"column":6,"free":true,"inReservation":true},{"row":9,"column":7,"free":true,"inReservation":true},{"row":9,"column":8,"free":true,"inReservation":true}]');
	INSERT INTO reservations VALUES (2, 'Red Eye', 2222, 'already@booked.de', 'Someone', '[{"row":9,"column":4,"free":true,"inReservation":true},{"row":9,"column":5,"free":true,"inReservation":true},{"row":9,"column":6,"free":true,"inReservation":true},{"row":9,"column":7,"free":true,"inReservation":true},{"row":9,"column":8,"free":true,"inReservation":true}]');
	INSERT INTO reservations VALUES (3, 'Lakes Outdoor', 3333, 'already@booked.de', 'Someone', '[{"row":9,"column":4,"free":true,"inReservation":true},{"row":9,"column":5,"free":true,"inReservation":true},{"row":9,"column":6,"free":true,"inReservation":true},{"row":9,"column":7,"free":true,"inReservation":true},{"row":9,"column":8,"free":true,"inReservation":true}]');
5. Setup config for XAMPP:
    in etc/httpd.conf:
      comment "Include etc/extra/httpd-vhosts.conf" in
      Change root directory:
          from
	    DocumentRoot "/opt/lampp/htdocs"
	    <Directory "/opt/lampp/htdocs">
	  to something like
	    DocumentRoot "/home/zwilling/webtech-dafot/assignment-4/task-2"
	    <Directory "/home/zwilling/webtech-dafot/assignment-4/task-2">
      In Linux you also have to change the user and group to your user and group if you have the solution files in your home folder
6. Restart XAMPP
7. Open localhost in your browser
      
