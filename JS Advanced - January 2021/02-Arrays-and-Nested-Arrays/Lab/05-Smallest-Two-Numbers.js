function solve(array) {
    array = array.sort((a, b) => a - b);
    console.log(`${array[0]} ${array[1]}`);
}