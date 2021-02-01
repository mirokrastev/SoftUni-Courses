function deleteByEmail() {
    let resultEl = document.getElementById('result');
    let input = document.querySelector('body > label:nth-child(2) > input:nth-child(1)').value;
    let allEmails = Array.from(document.getElementsByTagName('tbody')[0].children)
        .map(tr => tr.cells[1].textContent);
    if (!allEmails.includes(input)) {
        resultEl.textContent = 'Not found.';
        return;
    }
    document.getElementsByTagName('tbody')[0].children[allEmails.indexOf(input)].remove();
}