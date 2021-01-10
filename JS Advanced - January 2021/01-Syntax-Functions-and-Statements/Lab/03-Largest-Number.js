function solve(...args) {
    console.log(`The largest number is ${args.sort((a, b) => b - a)[0]}.`)
}