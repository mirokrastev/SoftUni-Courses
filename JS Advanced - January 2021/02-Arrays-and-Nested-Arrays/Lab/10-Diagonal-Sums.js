function solve(matrix) {
    let firstDiagonal = 0;
    let secondDiagonal = 0;

    for (let index = 0; index < matrix.length; index++) {
        firstDiagonal += matrix[index][index];
        secondDiagonal += matrix[index][(matrix.length-1)-index];
    }
    console.log(`${firstDiagonal} ${secondDiagonal}`);
}