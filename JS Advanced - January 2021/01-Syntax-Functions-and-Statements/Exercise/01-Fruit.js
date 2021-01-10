function solve(fruit, weightGrams, priceKg) {
    let result = weightGrams / 1000;
    console.log(`I need $${(result * priceKg).toFixed(2)} to buy ${result.toFixed(2)} kilograms ${fruit}.`)
}