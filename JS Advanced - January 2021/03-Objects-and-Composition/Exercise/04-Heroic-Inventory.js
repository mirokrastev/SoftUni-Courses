function solve(arr) {
    let jsonArr = [];

    for (let txt of arr) {
        let [name, level, items] = txt.split(' / ');
        items = items ? items.split(', ') : []
        level = Number(level);
        let obj = {name, level, items};
        jsonArr.push(obj);
    }
    console.log(JSON.stringify(jsonArr));
}