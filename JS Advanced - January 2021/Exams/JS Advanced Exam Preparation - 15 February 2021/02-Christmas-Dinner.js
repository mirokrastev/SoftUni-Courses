class ChristmasDinner {
    constructor(budget) {
        this.budget = budget;
        this.dishes = [];
        this.products = [];
        this.guests = {};
    }

    get budget() {
        return this._budget;
    }

    set budget(value) {
        if (value < 0) throw new Error('The budget cannot be a negative number');
        this._budget = value;
    }

    shopping(product) {
        let [productName, price] = product;
        if (price > this.budget) throw new Error('Not enough money to buy this product');
        this.products.push(productName);
        this.budget -= price;
        return `You have successfully bought ${productName}!`;
    }

    recipes(recipe) {
        recipe.productsList.forEach(product => {
            if (!this.products.includes(product)) throw new Error('We do not have this product');
        })
        this.dishes.push(recipe);
        return `${recipe.recipeName} has been successfully cooked!`;
    }

    inviteGuests(name, dish) {
        if (this.guests.hasOwnProperty(name)) throw new Error('This guest has already been invited');
        if (!this.dishes.find(e => e.recipeName === dish)) throw new Error('We do not have this dish');

        this.guests[name] = dish;

        return `You have successfully invited ${name}!`;
    }

    showAttendance() {
        let toReturn = [];

        for (let key of Object.keys(this.guests)) {
            let dish = this.dishes.find(e => e.recipeName === this.guests[key]);
            toReturn.push(`${key} will eat ${dish.recipeName}, which consists of ${dish.productsList.join(', ')}`);
        }
        return toReturn.join('\n');
    }
}