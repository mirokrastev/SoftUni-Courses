function solve(arr) {
    function appendMatrix() {
        for (let i = 0; i < row; i++) {
            let toAppend = [];

            for (let j = 0; j < col; j++) {
                toAppend.push(0);
            }
            matrix.push(toAppend);
        }
    }

    function makeCoord(row, col) {
        return {
            'up': [row-1, col], 'down': [row+1, col],
            'left': [row, col-1], 'right': [row, col+1],
            'upleft': [row-1, col-1], 'upright': [row-1, col+1],
            'downleft': [row+1, col-1], 'downright': [row+1, col+1]
        }
    }

    function makePrevCoords(previousNum) {
        let ll = [];
        for (let rowCounter = 0; rowCounter < row; rowCounter++) {
            for (let colCounter = 0; colCounter < col; colCounter++) {
                let currentNum = matrix[rowCounter][colCounter];

                if (currentNum == previousNum) {
                    ll.push([rowCounter, colCounter]);
                }
            }
        }
        return ll;
    }

    function process(dd, num) {
        for (let [row, col] of Object.values(dd)) {
            if (row <= -1 || col <= -1) {
                continue;
            }
            if (row >= matrix.length || col >= matrix.length) {
                continue;
            }

            currentNum = matrix[row][col]
            if (currentNum >= 1) {
                continue;
            }
            matrix[row][col] = num;
        }
    }

    function printMatrix() {
        for (let ll of matrix) {
            console.log(ll.join(" "));
        }
    }

    let [row, col, ...starCoord] = arr;
    let matrix = [];
    appendMatrix();
    matrix[starCoord[0]][starCoord[1]] = 1;
    let num = 2;
    process(makeCoord(starCoord[0], starCoord[1]), num);

    while (true) {
        let prevNumCoords = makePrevCoords(num);
        num++;

        if (prevNumCoords.length === 0) {
            break;
        }

        for (let [rowCounter, colCounter] of prevNumCoords) {
            process(makeCoord(rowCounter, colCounter), num)
        }
    }
    printMatrix();
}