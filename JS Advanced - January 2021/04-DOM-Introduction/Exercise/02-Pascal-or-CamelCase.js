function solve() {
    let text = document.getElementById('text').value
        .split(' ')
        .map(el => {
            el = el.toLowerCase();
            return el[0].toUpperCase() + el.slice(1);
        });
    let convention = document.getElementById('naming-convention').value;

    if (convention === 'Camel Case') {
        text[0] = text[0][0].toLowerCase() + text[0].slice(1);
    }
    if (!['Camel Case', 'Pascal Case'].includes(convention)) {
        text = ['Error!'];
    }
    document.getElementById('result').innerText = text.join('');
}