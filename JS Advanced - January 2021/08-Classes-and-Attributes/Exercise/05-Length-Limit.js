class Stringer {
    constructor(string, length) {
        this.innerString = string;
        this.innerLength = length;
    }

    increase(length) {
        this.innerLength += length;
    }

    decrease(length) {
        this.innerLength -= length;
        if (this.innerLength < 0) {
            this.innerLength = 0;
        }
    }

    toString() {
        let toDot = this.innerLength < this.innerString.length;

        if (toDot) {
            return `${this.innerString.slice(0, this.innerLength)}...`
        }
        return this.innerString;
    }
}