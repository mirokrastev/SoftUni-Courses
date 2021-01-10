function solve(numOne, numTwo) {
    numOne = Number(numOne);
    numTwo = Number(numTwo);
    let result = 0;

    for (let i = numOne; i <= numTwo; i++) {
        result += i;
    }
    console.log(result);
}