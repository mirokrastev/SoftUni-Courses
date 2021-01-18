function solve(array) {
    let currentBiggest = null;

    array.forEach(el => {
        if (currentBiggest === null) {
            currentBiggest = el;
        }
        if (el >= currentBiggest) {
            currentBiggest = el;
            console.log(el);
        }
    })
}