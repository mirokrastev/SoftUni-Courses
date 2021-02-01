function addItem() {
    let itemsMenu = document.getElementById('items');
    let toAdd = document.getElementById('newText');

    let newLiEl = document.createElement("li");
    newLiEl.innerHTML = `${toAdd.value} `;

    let deleteBtn = document.createElement('a');
    deleteBtn.innerHTML = '[Delete]';
    deleteBtn.href = '#';
    deleteBtn.addEventListener("click", (event) => event.target.parentElement.remove());

    newLiEl.appendChild(deleteBtn);

    itemsMenu.appendChild(newLiEl);
    toAdd.value = "";
}