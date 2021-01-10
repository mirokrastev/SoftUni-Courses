function solve(num) {
    let ll = []
    for (let temp = 0; temp < num; temp++) {
        ll.push('*')
    }

    for (let i = 0; i < num; i++) {
        console.log(ll.join(' '));
    }
}