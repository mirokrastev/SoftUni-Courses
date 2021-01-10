function solve(param) {
    if (!(typeof param === 'number')) {
        console.log(`We can not calculate the circle area, because we receive a ${typeof param}.`)
        return;
    }
    console.log(`${(Math.PI * (param*param)).toFixed(2)}`);
}