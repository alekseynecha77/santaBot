function updateCountdown() {
    const now = new Date();
    const currentYear = now.getFullYear();
    const christmas = new Date(currentYear, 11, 25); // Month is 0-indexed, 11 = December

    // If it's already Christmas, set to next year's Christmas
    if (now > christmas) {
        christmas.setFullYear(currentYear + 1);
    }

    const diff = christmas - now;

    let days = Math.floor(diff / (1000 * 60 * 60 * 24));
    let hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((diff % (1000 * 60)) / 1000);

    document.getElementById("countdownTimer").innerHTML = days + " days, " + hours + " hours, " + minutes + " minutes, " + seconds + " seconds ";
}

setInterval(updateCountdown, 1000);
