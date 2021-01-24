function sum() {
    let tBodyEl = document.querySelector('tbody');
    let resultEl = document.getElementById('sum');
    resultEl.textContent = Array.from(tBodyEl.rows)
                        .slice(1, tBodyEl.rows.length-1)
                        .reduce((a, c) => a + Number(c.cells[1].textContent), 0)
}