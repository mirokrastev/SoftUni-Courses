function addItem() {
    let inputField = document.querySelector('#newItemText');
    let listOutputs = document.getElementById('items');

    listOutputs.innerHTML += `<li>${inputField.value}</li>`
}