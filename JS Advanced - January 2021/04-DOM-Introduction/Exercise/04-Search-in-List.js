function search() {
    let matches = 0;
    let toSearch = document.getElementById('searchText').value;
    Array.from(document.getElementById('towns').children)
        .forEach(town => {
            if (town.textContent.includes(toSearch)) {
                town.style.fontWeight = 'bold';
                town.style.textDecoration = 'underline';
                matches++;
            }
         })
    document.getElementById('result').textContent = `${matches} matches found`;

}