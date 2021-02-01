function solution() {
    let initialString = '';

    return {
        append: (string) => initialString = initialString += string,

        removeStart: (index) => {
            if (!(Number.isInteger(index))) return;
            initialString = initialString.substring(index);
        },

        removeEnd: (index) => {
            if (!(Number.isInteger(index))) return;
            initialString = initialString.substring(0, initialString.length - index);
        },

        print: () => console.log(initialString),
    }
}