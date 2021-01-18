function solve(array) {
    function changeMatrix() {
        for (let index = 0; index < array.length; index++) {
            for (let col = 0; col < array.length; col++) {
                if (col === index || col === (array.length - 1) - index) continue;
                array[index][col] = mainDiagonal;
            }
        }
    }

    function printMatrix() {
        array.forEach(ll => console.log(ll.join(' ')));
    }
    
    array = array.map(row => row.split(' ').map(Number));
    let mainDiagonal, secondDiagonal;

    for (let index = 0; index < array.length; index++) {
        if (mainDiagonal === undefined) {
            mainDiagonal = array[index][index] - array[index][index];
        }
        if (secondDiagonal === undefined) {
            secondDiagonal = array[index][(array.length - 1) - index] - array[index][(array.length - 1) - index];
        }
        mainDiagonal += array[index][index];
        secondDiagonal += array[index][(array.length - 1) - index];
    }
    if (mainDiagonal !== secondDiagonal) {
        printMatrix();
        return;
    }
    changeMatrix();
    printMatrix();
}