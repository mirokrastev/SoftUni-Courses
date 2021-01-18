function solve(matrix) {
    let newArray = []
    matrix.forEach(row => newArray.push(Math.max(...row)));
    console.log(Math.max(...newArray));
}