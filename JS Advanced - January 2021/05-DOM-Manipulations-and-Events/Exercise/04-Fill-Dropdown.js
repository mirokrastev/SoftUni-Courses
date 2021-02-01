function addItem() {
    let textContentEl = document.getElementById('newItemText');
    let valueContentEl = document.getElementById('newItemValue');

    let newOption = document.createElement('option')
    newOption.textContent = textContentEl.value;
    newOption.value = valueContentEl.value;

    textContentEl.value = '';
    valueContentEl.value = '';
    let menuEl = document.getElementById('menu');
    menuEl.appendChild(newOption);
}