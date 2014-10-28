/**
 * @author Frederik Zwilling
 */

function drawReservationCanvas() {
	var canvas = document.getElementById("can-reservation");
	var ctx = canvas.getContext("2d");
	//background
	ctx.fillStyle = "#4BA9F0";
	ctx.fillRect(0, 0, canvas.width, canvas.height);

	//draw screen
	ctx.fillStyle = "#FFFFFF";
	ctx.fillRect(canvas.width / 5, 10, canvas.width * 3 / 5, 30);
	ctx.font = "bold 20px sans-serif";
	ctx.fillStyle = "#000000";
	ctx.textAlign = "center";
	ctx.fillText("Screen", canvas.width / 2, 30);

	//draw some seats
	var seat_free = new Image();
	var seat_booked = new Image();
	seat_free.src = "images/seat-free.png";
	seat_booked.src = "images/seat-booked.png";
	var rows = 10;
	var cols = 16;
	for ( i = 0; i < rows; i++) {
		for ( j = 0; j < cols; j++) {
			var posx = canvas.width / 2 - seat_free.width * (j - cols / 2 + 1);
			var posy = 80 + i * seat_free.height;
			ctx.drawImage(seat_free, posx, posy);
		}
	}
}