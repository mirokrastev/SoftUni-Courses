function solve(input) {
    function carsBuilder() {
        let objs = {};

        return (command, model, ...args) => {
            let create = (model, toInheritCommand, parentClass) => {
                objs[model] = {initial: {}};
                if (toInheritCommand) {
                    objs[model].toInherit = objs[parentClass];
                }
            }
            let set = (model, toSetKey, toSetValue) => {
                objs[model].initial[toSetKey] = toSetValue;
            }
            let print = model => {
                let carModelObj = objs[model];
                let carModel;

                if (carModelObj.toInherit) {
                    let test = carModelObj.toInherit
                    if (test.hasOwnProperty('toInherit')) {
                        carModel = {...carModelObj.initial, ...carModelObj.toInherit.initial, ...carModelObj.toInherit.toInherit.initial};
                    }
                    else {
                        carModel = {...carModelObj.initial, ...carModelObj.toInherit.initial};
                    }
                }
                else {
                    carModel = carModelObj.initial;
                }
                console.log(Object.entries(carModel)
                    .map(([key, value]) => `${key}:${value}`)
                    .join(', '))
            };

            if (command === 'create') {
                create(model, ...args);
            }
            else if (command === 'set') {
                set(model, ...args);
            }
            else if (command === 'print') {
                print(model);
            }
        }
    }

    let carsWrapper = carsBuilder();
    input.forEach(string => carsWrapper(...string.split(' ')));
}