function solve(arr) {
    let sumResult = arr.reduce((a, x) => a + x, 0);
    let sumInverse = arr.reduce((a, x) => a + (1 / x), 0);
    let concat = arr.reduce((a, x) => a + x, '');
    console.log(sumResult);
    console.log(sumInverse);
    console.log(concat);
}