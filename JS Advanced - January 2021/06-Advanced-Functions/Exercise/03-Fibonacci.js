function getFibonator() {
    let a = 1;
    let b = 0;

    return () => {
        let temp = a;
        a = a + b;
        b = temp;
        return b;
    }
}