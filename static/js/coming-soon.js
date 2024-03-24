
// Set the date and time to count down to
var countDownDate = new Date("August 1, 2024 00:00:00").getTime();
// Update the countdown every 1 second
var countdown = setInterval(function () {

    // Get the current date and time
    var now = new Date().getTime();

    // Calculate the distance between the current date/time and the countdown date/time
    var distance = countDownDate - now;

    // Calculate days, hours, minutes, and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("days-number").innerHTML = days;
    document.getElementById("hours-number").innerHTML = hours;
    document.getElementById("minutes-number").innerHTML = minutes;
    document.getElementById("seconds-number").innerHTML = seconds;
    // If the countdown is finished, display a message
    if (distance < 0) {
        clearInterval(countdown);
        document.getElementById("countdown").innerHTML = "Launched";
    }
}, 1000);