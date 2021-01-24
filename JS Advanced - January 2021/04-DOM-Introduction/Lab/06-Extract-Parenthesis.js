function extract() {
    let contentEl = document.getElementById('content').innerText;
    let wordsArray = [];
    let toSlice = 0;

    for (let index = 0; index < contentEl.length; index++) {
        let char = contentEl[index];
        if (char === '(') {
            toSlice = index+1;
        }
        else if (char === ')') {
            wordsArray.push(contentEl.slice(toSlice, index));
            toSlice = 0;
        }
    }
    return wordsArray.join('; ');
}