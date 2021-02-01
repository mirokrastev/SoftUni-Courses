function solve(...args) {
    let dd = {};

    args.forEach(arg => {
        let argType = typeof arg;
        if (!dd.hasOwnProperty(argType)) {
            dd[argType] = 0;
        }
        dd[argType]++;
        try {
            console.log(`${argType}: ${arg.toString()}`);
        }
        catch (TypeError) {
            console.log(`${argType}: ${arg}`);
        }
    })
    Object.keys(dd)
        .sort((a, b) => dd[b] - dd[a])
        .forEach(key => console.log(`${key} = ${dd[key]}`));
}