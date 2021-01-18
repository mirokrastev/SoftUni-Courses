function solve(matrix) {
    function calculateNeighbour(row, col) {
        let initial = matrix[row][col];
        let cc = 0;
        let mapper = {0: [row+1, col], 1: [row, col-1],
                      2: [row, col+1], 3: [row-1, col]};
        for (let i = 0; i < Object.keys(mapper).length; i++) {
            try {
                let coord = mapper[i];
                let toCompare = matrix[coord[0]][coord[1]];
                if (toCompare === null) continue;
                if (initial === toCompare) {
                    cc++;
                }
            }
            catch (TypeError) {
                continue;
            }
        }
        matrix[row][col] = null;
        return cc;
    }

    let cc = 0;

    for (let row = 0; row < matrix.length; row++) {
        for (let col = 0; col < matrix[0].length; col++) {
            cc += calculateNeighbour(row, col);
        }
    }
    console.log(cc);
}