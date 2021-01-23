function solve(input) {
    let notations = [];
    let mapper = {
        '+': (x, y) => x + y,
        '-': (x, y) => x - y,
        '*': (x, y) => x * y,
        '/': (x, y) => x / y
    }

    function calculate(operator) {
        let [numOne, numTwo] = [notations.pop(), notations.pop()];
        if (numOne === undefined || numTwo === undefined) {
            return false;
        }
        return mapper[operator](numTwo, numOne);
    }

    for (let el of input) {
        if (typeof el === 'number') {
            notations.push(el);
            continue;
        }
        let funcResult = calculate(el);
        if (funcResult === false) {
            console.log(`Error: not enough operands!`);
            return;
        }
        notations.push(funcResult);
    }
    if (notations.length > 1) {
        console.log(`Error: too many operands!`);
        return;
    }
    console.log(notations[0]);
}