function solve(n, k) {
    let arr = [1];

    for (let i = 0; i < n-1; i++) {
        let startIndex = (i+1) - k;
        startIndex = startIndex >= 0 ? startIndex : 0;
        let sum = arr.slice(startIndex, i+1);
        arr.push(sum.reduce((a, x) => a+x, 0));
    }
    return arr;
}