function generateReport() {
    const checks = document.querySelectorAll('input[type="checkbox"]');
    const data = Array.from(document.querySelectorAll('tbody>tr'))
        .map(r => Array.from(r.children)
        .reduce((acc, col, i) => Object.assign(acc, checks[i].checked ? {[checks[i].name]: col.textContent} : {}), {}));

    document.getElementById('output').textContent = JSON.stringify(data, null, 2);
}