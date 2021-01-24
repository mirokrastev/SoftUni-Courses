function colorize() {
    let tableEl = document.querySelector('table');
    Array.from(tableEl.rows)
        .slice(1)
        .forEach(function(row, index) {
        if (index % 2 === 0) {
            row.setAttribute('style', 'background:Teal');
        }
    })
}