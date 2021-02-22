function solve(input, sortingCriteria) {
    class Ticket {
        constructor(destination, price, status) {
            this.destination = destination;
            this.price = price;
            this.status = status;
        }
    }

    return input.map(entry => {
        let [destination, price, status] = entry.split('|');
        return new Ticket(destination, Number(price), status);
    }).sort((a, b) => {
        if (sortingCriteria === 'price') {
            return a[sortingCriteria] - b[sortingCriteria];
        }
        return a[sortingCriteria].localeCompare(b[sortingCriteria]);
    })
}