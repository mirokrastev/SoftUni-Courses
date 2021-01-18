function solve(arr) {
    let cc = -1;
    console.log(arr.filter(_ => {
        cc++;
        if (cc % 2 === 0) {
            return true;
        }
        return false;
    }).join(' '));
}