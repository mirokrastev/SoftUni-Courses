function editElement(htmlEl, toReplace, newMessage) {
    while (htmlEl.innerText.includes(toReplace)) {
        htmlEl.innerText = htmlEl.innerText.replace(toReplace, newMessage);
    }
}