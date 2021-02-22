class List {
    constructor() {
        this.list = [];
    }

    add(element) {
        this.list.push(element);
        this.list.sort((a, b) => a - b);
    }

    remove(index) {
        if (index >= this.list.length || index <= -1) return;
        this.list.splice(index, 1);
    }

    get(index) {
        if (index >= this.list.length || index <= -1) return;
        return this.list[index];
    }

    get size() {
        return this.list.length;
    }

    hasOwnProperty() {
        return true;
    }
}