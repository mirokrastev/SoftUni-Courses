function solve(input) {
    let rawInput = {};
    let juicesMade = {};

    input.forEach(entry => {
        let [juiceName, juiceQuantity] = entry.split(' => ');
        if (!rawInput.hasOwnProperty(juiceName)) {
            rawInput[juiceName] = 0;
        }
        rawInput[juiceName] += Number(juiceQuantity);
        createJuice(juiceName)
    })

    function createJuice(juiceName) {
        while (rawInput[juiceName] >= 1000) {
            if (!juicesMade.hasOwnProperty(juiceName)) {
                juicesMade[juiceName] = 0;
            }
            rawInput[juiceName] -= 1000;
            juicesMade[juiceName]++;
        }
    }

    Object.keys(juicesMade).forEach(key => console.log(`${key} => ${juicesMade[key]}`));
}