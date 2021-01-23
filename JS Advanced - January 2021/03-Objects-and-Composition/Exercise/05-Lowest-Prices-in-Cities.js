function solve(arr) {
    let obj = {};

    for (let i of arr) {
        let [town, product, price] = i.split(' | ');
        price = Number(price);

        if (!obj.hasOwnProperty(product)) {
            obj[product] = [price, town];
            continue;
        }
        if (price < obj[product][0]) {
            obj[product] = [price, town];
        }
    }

    for (let [key, ll] of Object.entries(obj)) {
        console.log(`${key} -> ${ll[0]} (${ll[1]})`);
    }
}