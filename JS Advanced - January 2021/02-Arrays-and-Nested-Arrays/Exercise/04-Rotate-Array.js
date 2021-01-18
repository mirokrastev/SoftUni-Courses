function solve(array, rotations) {
    let toRotate = Number(rotations);
    if (toRotate % array.length === 0) {
        console.log(array.join(' '));
        return;
    }

    let toStart = array.length;

    for (let i = 0; i < toRotate; i++) {
        toStart--;
        if (toStart <= -1) toStart = array.length-1;
    }
    console.log([...array.slice(toStart, array.length), ...array.slice(0, toStart)].join(' '));
}