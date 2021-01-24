function toggle() {
    let spanEl = document.getElementsByClassName('button')[0];
    let textId = document.getElementById('extra');

    if (spanEl.innerHTML === 'More') {
        spanEl.innerHTML = 'Less';
        textId.style.display = 'block';
        return;
    }
    spanEl.innerHTML = 'More';
    textId.style.display = 'none';
}