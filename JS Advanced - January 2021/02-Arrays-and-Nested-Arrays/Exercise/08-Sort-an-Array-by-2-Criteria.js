function solve(array) {
    array.sort((a, b) => {
        if (a.length === b.length) {
            return (a.toLowerCase().localeCompare(b.toLowerCase()));
        }
        return a.length - b.length;
    }).forEach(entry => console.log(entry))
}