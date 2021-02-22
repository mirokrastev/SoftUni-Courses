function solve(input) {
    let output = {};
    input.forEach(entry => {
        let [carBrand, carModel, producedCars] = entry.split(' | ');
        if (!output.hasOwnProperty(carBrand)) {
            output[carBrand] = {};
        }
        if (!output[carBrand].hasOwnProperty(carModel)) {
            output[carBrand][carModel] = 0;
        }
        output[carBrand][carModel] += Number(producedCars);
    })
    Object.keys(output).forEach(key => {
        console.log(key);
        Object.keys(output[key]).forEach(model => {
            console.log(`###${model} -> ${output[key][model]}`);
        })
    })
}