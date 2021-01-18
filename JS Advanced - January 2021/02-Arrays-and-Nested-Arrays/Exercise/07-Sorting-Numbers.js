function solve(array) {
    let finalArray = [];

    while (array.length > 0) {
        let toAdd;
        if (finalArray.length % 2 === 0) {
            toAdd = Math.min(...array);
        }
        else {
            toAdd = Math.max(...array);
        }
        array.splice(array.indexOf(toAdd), 1);
        finalArray.push(toAdd);
    }
    return finalArray;
}