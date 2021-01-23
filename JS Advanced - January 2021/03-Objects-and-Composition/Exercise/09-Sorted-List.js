function createSortedList() {
    class SortedList {
        constructor() {
            this.ll = [];
        }
        sortList() {
            this.ll.sort((a, b) => (a - b));
        }
        add(element) {
            this.ll.push(element);
            this.sortList();
        }
        remove(index) {
            if (index < 0 || index >= this.ll.length) return;
            this.ll.splice(index, 1);
            this.sortList();
        }
        get size() {
            return this.ll.length;
        }
        get(index) {
            if (index < 0 || index >= this.ll.length) return;
            return this.ll[index];
        }

        hasOwnProperty(value) {
            return value in this
        }
    }
    return new SortedList();
}