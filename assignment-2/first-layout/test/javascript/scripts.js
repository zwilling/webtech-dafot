/**
* Set cinema coordinates to storage
**/
window.onload = function(e) {
	var cinemas = {
		'collection': [
			{
				'cinema_name' : 'IMAX',
				'lat': 50.777477,
				'lon': 6.078240
			},
			{
				'cinema_name': 'Cinema City',
				'lat': 50.759564,
				'lon': 6.072994
			},
			{
				'cinema_name': 'National Cinema',
				'lat': 50.779663,
				'lon': 6.102961
			}
		]
	};
	localStorage.setItem('cinemas', JSON.stringify(cinemas));
}

function initReservatioCanvas() {
	//create canvas element and context to draw in
	canvasReservation = document.getElementById("can-reservation");
	contextReservation = canvasReservation.getContext("2d");

	//get images for seats
	seat_free = new Image();
	seat_booked = new Image();
	seat_free.src = "images/seat-free.png";
	seat_booked.src = "images/seat-booked.png";

	//init some global variables
	rows = 10;
	cols = 16;

	//add on click event
	canvasReservation.addEventListener("click", clickOnReservationCanvas, false);
	
	//draw reservations when the seat-picture is loaded
	seat_free.onload = function(){
		seatOffsetX = canvasReservation.width / 2 - seat_free.width * (cols / 2);
		seatOffsetY = 80;
		drawReservationCanvas();
	};
}

/**
 * Draw or update the Reservation canvas
 */
function drawReservationCanvas() {
	var ctx = contextReservation;
	//background
	ctx.fillStyle = "#4BA9F0";
	ctx.fillRect(0, 0, canvasReservation.width, canvasReservation.height);

	//draw screen
	ctx.fillStyle = "#FFFFFF";
	ctx.fillRect(canvasReservation.width / 5, 10, canvasReservation.width * 3 / 5, 30);
	ctx.font = "bold 20px sans-serif";
	ctx.fillStyle = "#000000";
	ctx.textAlign = "center";
	ctx.fillText("Screen", canvasReservation.width / 2, 30);

	//draw seats
	for ( i = 0; i < rows; i++) {
		for ( j = 0; j < cols; j++) {
			var posx = seatOffsetX + j * seat_free.width;
			var posy = seatOffsetY + i * seat_free.height;
			ctx.drawImage(seat_free, posx, posy);
		}
	}
}

/**
 * What happens when a user clicks on the reservation canvas?
 *
 * Currently we just turn green seats into red ones
 */
function clickOnReservationCanvas(e) {
	var ctx = contextReservation;
	
	//get seat number
	var seat = getSeatFromClick(e);
	if(seat.row < 0 || seat.column < 0 || seat.row >= rows || seat.column >= cols){
		return;
	}

	//draw red seat over the green one
	var posx = seatOffsetX + seat.column * seat_free.width;
	var posy = seatOffsetY + seat.row * seat_free.height;
	ctx.drawImage(seat_booked, posx, posy);
}

/**
 * Calculate on which seat the user clicked
 * @param {Object} e
 */
function getSeatFromClick(e) {
	var x;
	var y;
	if (e.pageX != undefined && e.pageY != undefined) {
		x = e.pageX;
		y = e.pageY;
	} else {
		x = e.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
		y = e.clientY + document.body.scrollTop + document.documentElement.scrollTop;
	}
	x -= canvasReservation.offsetLeft + seatOffsetX;
	y -= canvasReservation.offsetTop + seatOffsetY;

	//find seat number
	x = Math.floor(x / seat_free.width);
	y = Math.floor(y / seat_free.height);
	var seat = new Seat(x, y);
	return seat;
}

/**
 * "Class" definition of Seats
 * @param {Object} column
 * @param {Object} row
 */
function Seat(column, row) {
	this.row = row;
	this.column = column;
}

// Geolocation
/**
* Select nearest cinema according to user coords
**/
function chooseNearestCinema() {
	if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(findNearestCinema);
    } else {
        // red popovers
    }
}

/**
* Find nearest cinema according to user coordinates and save to storage
**/
function findNearestCinema(position) {
	var storage = localStorage.getItem('cinemas');
	var cinemas = JSON.parse(storage);
	var smallestDistance = null;
	var nearestCinema = null;

	for (var i = 0; i < cinemas.collection.length; i++) {
		var distance = countDistance(
				position.coords.latitude, position.coords.longitude, 
				cinemas.collection[i].lat, cinemas.collection[i].lon
			);
		if (smallestDistance == null) {
			smallestDistance = distance;
			nearestCinema = cinemas.collection[i].cinema_name;
		}
		else {
			if (distance < smallestDistance) {
				smallestDistance = distance;
				nearestCinema = cinemas.collection[i].cinema_name;
			}
		}
	}
	localStorage.setItem('chosen_cinema', nearestCinema);
	expandCinameOptions(nearestCinema);
}

/**
* Count distance between two points
**/
function countDistance(lat1, lon1, lat2, lon2) {
	var R = 6371;
  	var a = 0.5 - Math.cos((lat2 - lat1) * Math.PI / 180)/2 + 
    	Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) * 
    	(1 - Math.cos((lon2 - lon1) * Math.PI / 180))/2;

  	return R * 2 * Math.asin(Math.sqrt(a));
}

/**
* Select cinema with button
**/
function chooseCinemaOnButtonSelect() {
//set cinema to localstorage
}

/**
* Show all options of selected cinema (movies slider, reservation)
**/
function expandCinemaOptions() {

}
