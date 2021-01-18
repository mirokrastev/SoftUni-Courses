function solve(array) {
    let newArray = [];
    for (let index = 0; index < array.length; index++) {
        if (index % 2 === 1) {
            newArray.splice(0, 0, array[index] * 2);
        }
    }
    console.log(newArray.join(' '));
}