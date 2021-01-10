function solve(num) {
    let map = {};
    let result = 0;
    for (let str of String(num)) {
        map[str] = null;
        result += Number(str);
    }
    console.log(Object.keys(map).length === 1);
    console.log(result);
}