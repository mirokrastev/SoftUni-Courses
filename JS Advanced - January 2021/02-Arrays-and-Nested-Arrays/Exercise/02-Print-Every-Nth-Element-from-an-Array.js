function solve(arr) {
    let step = Number(arr.pop());

    for (let i = 0; i < arr.length; i += step) {
        console.log(arr[i]);
    }
}