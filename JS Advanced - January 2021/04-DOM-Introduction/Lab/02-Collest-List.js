function extractText() {
    let textAreaEl = document.getElementById('result');
    let textElements = Array.from(document.getElementById('items')
        .children)
        .map(docEl => docEl.innerText);
    textAreaEl.innerHTML = textElements.join('\n');
}