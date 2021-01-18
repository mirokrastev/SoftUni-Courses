function solve(array) {
    let initialNum = 1;
    let ll = [];

    array.forEach(command => {
        if (command === 'add') {
            ll.push(initialNum);
        }
        else if (command === 'remove') {
            if (ll.length >= 1) {
                ll.pop();
            }
        }
        initialNum++;
    })
    if (ll.length === 0) {
        console.log('Empty');
        return;
    }
    console.log(ll.join('\n'));
}
