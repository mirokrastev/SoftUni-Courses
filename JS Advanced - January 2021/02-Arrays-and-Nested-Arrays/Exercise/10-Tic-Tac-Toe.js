function solve(coordinates) {
    const winningCoords = [[0, 1, 2], [0, 3, 6], [0, 4, 8],
                           [1, 4, 7], [2, 5, 8], [2, 4, 6],
                           [3, 4, 5], [6, 7, 8]]
    const mapChar = {0: 'X', 1: 'O'};
    const mapFirstCoord = {'0': 0, '1': 3, '2': 6}


    function processInp(coord, char) {
        if (!(ticTacToe[coord])) {
            ticTacToe[coord] = char;
            freeCoords.splice(freeCoords.indexOf(coord), 1);
            let outputWin = checkWin(char)
            if (outputWin === 'no more room') {
                return 'no more room';
            }
            if (outputWin) {
                return 'stop';
            }
            return true;
        }
        console.log("This place is already taken. Please choose another!");
        return false;
    }

    function checkWin(char) {
        for (let i of winningCoords) {
            let combo = `${ticTacToe[i[0]]} ${ticTacToe[i[1]]} ${ticTacToe[i[2]]}`;

            if (['X X X', 'O O O'].includes(combo)) {
                console.log(`Player ${char} wins!`);
                printTicTacToe();
                return true;
            }
        }
        if (freeCoords.length === 0) {
            return 'no more room'
        }
        return false;
    }

    function printTicTacToe() {
        console.log(`${ticTacToe[0]}\t${ticTacToe[1]}\t${ticTacToe[2]}`);
        console.log(`${ticTacToe[3]}\t${ticTacToe[4]}\t${ticTacToe[5]}`);
        console.log(`${ticTacToe[6]}\t${ticTacToe[7]}\t${ticTacToe[8]}`);
    }

    function draw() {
        console.log('The game ended! Nobody wins :(');
        printTicTacToe();
    }

    let ticTacToe = [
        false, false, false,
        false, false, false,
        false, false, false
    ]
    let freeCoords = [0, 1, 2, 3, 4, 5, 6, 7, 8];
    let index = 0;
    for (let inp of coordinates) {
        if (index >= 2) { index = 0; }
        let [row, col] = inp.split(' ');
        let actualCoord = mapFirstCoord[row] + Number(col);
        let output = processInp(actualCoord, mapChar[index]);
        if (output === 'no more room') {
            draw();
            return;
        }
        if(!output) {
            continue;
        }
        if (output === 'stop') { return; }
        index++;
    }
}