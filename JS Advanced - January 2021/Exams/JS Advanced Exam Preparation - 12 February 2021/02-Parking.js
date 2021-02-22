class Parking {
    constructor(capacity) {
        this.capacity = capacity;
        this.vehicles = [];
    }

    addCar(carModel, carNumber) {
        if (this.vehicles.length >= this.capacity)
            throw new Error('Not enough parking space.');
        this.vehicles.push({carModel, carNumber, payed: false});
        return `The ${carModel}, with a registration number ${carNumber}, parked.`;
    }

    removeCar(carNumber) {
        let car = this.vehicles.find(e => e.carNumber === carNumber);
        if (car === undefined)
            throw new Error('The car, you\'re looking for, is not found.');
        if (!car.payed)
            throw new Error(`${car.carNumber} needs to pay before leaving the parking lot.`);
        this.vehicles.splice(this.vehicles.indexOf(car), 1);
        return `${car.carNumber} left the parking lot.`;
    }

    pay(carNumber) {
        let car = this.vehicles.find(e => e.carNumber === carNumber);
        if (car === undefined)
            throw new Error(`${carNumber} is not in the parking lot.`);
        if (car.payed)
            throw new Error(`${carNumber}\'s driver has already payed his ticket.`);
        car.payed = true;
        return `${carNumber}\'s driver successfully payed for his stay.`;
    }

    getStatistics(carNumber) {
        let toReturn = [];
        if (carNumber === undefined) {
            toReturn.push(`The Parking Lot has ${this.capacity - this.vehicles.length} empty spots left.`);
            this.vehicles.sort((a, b) => a.carNumber.localeCompare(b.carNumber))
                .forEach(car => {
                    toReturn.push(`${car.carModel} == ${car.carNumber} - ${car.payed ? "Has" : "Not"} payed`);
                })
        }
        else {
            let car = this.vehicles.find(e => e.carNumber === carNumber);
            toReturn.push(`${car.carModel} == ${car.carNumber} - ${car.payed ? "Has" : "Not"} payed`);
        }
        return toReturn.join('\n');
    }
}