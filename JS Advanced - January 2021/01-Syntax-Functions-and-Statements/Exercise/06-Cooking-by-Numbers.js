function solve(num, ...args) {
    let result = Number(num);
    let mapper = {'chop': (numArg) => numArg / 2, 'dice': (numArg) => Math.sqrt(numArg),
                  'spice': (numArg) => numArg + 1, 'bake': (numArg) => numArg * 3,
                  'fillet': (numArg) => (numArg * 0.8).toFixed(1)}

    args.forEach((arg) => {
        result = mapper[arg](result);
        console.log(result);
    })
}