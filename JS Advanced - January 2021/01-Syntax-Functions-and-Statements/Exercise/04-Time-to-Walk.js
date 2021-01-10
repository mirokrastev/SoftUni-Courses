function solve(steps, studentFootprintLength, studentSpeed) {
    let distanceMeters = steps * studentFootprintLength;
    let speedMetersSec = studentSpeed / 3.6;
    let time = distanceMeters / speedMetersSec;
    let rest = Math.floor(distanceMeters / 500);

    let timeMin = Math.floor(time / 60);
    let timeSec = Math.round(time - (timeMin * 60));
    let timeHr = Math.floor(time / 3600);

    timeMin += rest;

    while (timeMin >= 60) {
        timeMin -= 60;
        timeHr++;
    }

    let outputHr = timeHr >= 10 ? timeHr : `0${timeHr}`;
    let outputMin = timeMin >= 10 ? timeMin : `0${timeMin}`;
    let outputSec = timeSec >= 10 ? timeSec : `0${timeSec}`;

    console.log(`${outputHr}:${outputMin}:${outputSec}`);
}