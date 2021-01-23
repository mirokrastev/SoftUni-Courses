function solve(input) {
    let engineVolume = {90: 1800, 120: 2400, 200: 3500}
    let wheel = input.wheelsize;
    wheel = wheel % 2 === 1 ? wheel : wheel - 1;
    (() => {
        if (engineVolume.hasOwnProperty(input.power)) return;
        let enginePower = input.power;
        for (let key of Object.keys(engineVolume)) {
            if (key >= enginePower) {
                input.power = Number(key);
                return;
            }
        }
    })()
    
    return {
        model: input.model,
        engine: {
            power: input.power,
            volume: engineVolume[input.power]
        },
        carriage: {
            type: input.carriage,
            color: input.color
        },
        wheels: [wheel, wheel, wheel, wheel]
    }
}