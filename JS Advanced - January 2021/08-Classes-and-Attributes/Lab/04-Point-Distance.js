class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    static distance(instOne, instTwo) {
        return Math.sqrt((instOne.x - instTwo.x) ** 2 + (instOne.y - instTwo.y) ** 2);
    }
}