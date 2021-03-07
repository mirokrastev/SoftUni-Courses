const phonebookEl = document.getElementById('phonebook');
const loadButton = document.getElementById('btnLoad');
const createButton = document.getElementById('btnCreate');

const personNameField = document.getElementById('person');
const personPhone = document.getElementById('phone');

loadButton.addEventListener('click', loadContacts);
createButton.addEventListener('click', addContact);

async function loadContacts() {
    phonebookEl.innerHTML = '';
    let response = await fetch(`http://localhost:3030/jsonstore/phonebook`);
    Object.values((await response.json()))
        .forEach(obj => {
            let newLi = document.createElement('li');
            newLi.textContent = `${obj.person}:${obj.phone}`;
            let delButton = document.createElement('button');
            delButton.textContent = 'Delete';
            delButton.addEventListener('click', async () => await deleteContact(obj._id))
            newLi.appendChild(delButton);
            phonebookEl.appendChild(newLi);
        });
}

async function addContact() {
    if (!personNameField.value || !personPhone.value)
        return alert('Invalid contact!');
    await fetch(`http://localhost:3030/jsonstore/phonebook`, {
        method: 'POST',
        body: JSON.stringify({person: personNameField.value, phone: personPhone.value})
    });
    personNameField.value = '';
    personPhone.value = '';
    await loadContacts();
}

async function deleteContact(contactId) {
    await fetch(`http://localhost:3030/jsonstore/phonebook/${contactId}`, {
        method: 'DELETE',
    });
    await loadContacts();
}

loadContacts();