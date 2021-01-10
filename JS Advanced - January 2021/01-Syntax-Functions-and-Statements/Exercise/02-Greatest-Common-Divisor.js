function solve(numOne, numTwo) {
    if (!numTwo) {
        console.log(numOne);
        return;
    }
    return solve(numTwo, numOne % numTwo);
}