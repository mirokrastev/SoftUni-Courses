function solve(x1, y1, x2, y2) {
    function isInteger(x1, y1, x2, y2) {
        let distance = Math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2));
        return distance % 1 === 0;
    }

    function calculateDistance(x1, y1, x2, y2) {
        if (isInteger(x1, y1, x2, y2)) {
            return `{${x1}, ${y1}} to {${x2}, ${y2}} is valid`;
        }

        return `{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`;
    }

    console.log(calculateDistance(x1, y1, 0, 0));
    console.log(calculateDistance(x2, y2, 0, 0));
    console.log(calculateDistance(x1, y1, x2, y2));
}