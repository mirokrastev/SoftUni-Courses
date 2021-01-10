function solve(speed, area) {
    let map = {'motorway': 130, 'interstate': 90, 'city': 50, 'residential': 20};
    let allowed = map[area];

    if (allowed >= speed) {
        console.log(`Driving ${speed} km/h in a ${allowed} zone`);
        return;
    }
    let diff = speed - allowed;
    let status;

    if (diff <= 20) {
        status = 'speeding';
    }
    else if (diff <= 40) {
        status = 'excessive speeding';
    }
    else {
        status = 'reckless driving';
    }

    console.log(`The speed is ${diff} km/h faster than the allowed speed of ${allowed} - ${status}`)
}