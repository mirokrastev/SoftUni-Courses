function solve(array) {
    let newArray = [];
    array.forEach(el => {
        if (el >= 0) {
            newArray.push(el);
        }
        else {
            newArray.splice(0, 0, el);
        }
    })
    newArray.forEach(el => console.log(el));
}