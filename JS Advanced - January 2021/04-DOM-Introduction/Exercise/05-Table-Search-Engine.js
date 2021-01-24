function solve() {
    let tBodyEl = document.getElementsByTagName('tbody')[0];
    let searchBtn = document.getElementById('searchBtn');
    let searchField = document.getElementById('searchField');
    searchBtn.addEventListener('click', traverseTable);
 
    function traverseTable() {
        let wordToSearch = searchField.value;
        for (let row of Array.from(tBodyEl.children)) {
            let match = false;
            for (let column of Array.from(row.children)) {
                if (column.textContent.includes(wordToSearch)) {
                    row.setAttribute('class', 'select');
                    match = true;
                }
            }
            if (!match) {
                row.removeAttribute('class');
            }
        }
        searchField.value = '';
    }
 }