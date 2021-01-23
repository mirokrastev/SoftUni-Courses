function solve(arr) {
    let nestedObj = {};

    for (let txt of arr) {
        let [itemName, price] = txt.split(' : ');
        let charItemName = itemName[0]
        if (!nestedObj.hasOwnProperty(charItemName)) {
            nestedObj[charItemName] = {};
        }
        nestedObj[charItemName][itemName] = Number(price);
    }
    nestedObj = Object.entries(nestedObj).sort()
    for (let arr of nestedObj) {
        console.log(arr[0])
        for (let [key, value] of Object.entries(arr[1]).sort()) {
            console.log(`  ${key}: ${value}`);
        }
    }
}