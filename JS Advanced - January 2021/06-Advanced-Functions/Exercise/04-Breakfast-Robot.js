function solution() {
    let products = {
        'apple': {
            'carbohydrate': 1,
            'flavour': 2
        },
        'lemonade': {
            'carbohydrate': 10,
            'flavour': 20
        },
        'burger': {
            'carbohydrate': 5,
            'fat': 7,
            'flavour': 3
        },
        'eggs': {
            'protein': 5,
            'fat': 1,
            'flavour': 1
        },
        'turkey': {
            'protein': 10,
            'carbohydrate': 10,
            'fat': 10,
            'flavour': 10
        }
    }
    let microElements = {
        'protein': 0,
        'carbohydrate': 0,
        'fat': 0,
        'flavour': 0
    }

    return (input) => {
        let [command, microEl, quantity] = input.split(' ');
        if (command === 'report') {
            let ll = []
            Object.keys(microElements).forEach((key) => ll.push(`${key}=${microElements[key]}`))
            return ll.join(' ');
            return;
        }

        if (command === 'restock') {
            microElements[microEl] += Number(quantity);
            return 'Success';
        } else if (command === 'prepare') {
            let currentElement = Object.keys(products[microEl]);
            let toBreak = false;

            for (i = 0; i < Number(quantity); i++) {
                for (let key of Array.from(currentElement)) {
                    if (products[microEl][key] > microElements[key]) {
                        toBreak = true;
                    }
                    if (toBreak) {
                        return `Error: not enough ${key} in stock`;
                    }
                }
                if (!toBreak) {
                    for (let key of Array.from(currentElement)) {
                        microElements[key] -= products[microEl][key]
                    }
                }
            }
            return 'Success';
        }
    }
}