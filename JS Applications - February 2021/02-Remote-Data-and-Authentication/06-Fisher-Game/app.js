const loadButton = document.getElementById('load');
loadButton.addEventListener('click', loadCatches);

const catchesDiv = document.getElementById('catches');

const authToken = sessionStorage.getItem('authToken');
const userId = sessionStorage.getItem('userId');

if (authToken !== null) {
    let guestDiv = document.getElementById('guest');
    guestDiv.innerHTML = '';

    let newAnchor = document.createElement('a');
    newAnchor.textContent = 'Logout';
    newAnchor.addEventListener('click', () => {
        sessionStorage.removeItem('authToken');
        sessionStorage.removeItem('userId');
        window.location.pathname = '06.Fisher-Game/index.html';
    })
    guestDiv.appendChild(newAnchor);

    const addButton = document.getElementById('add')
    addButton.removeAttribute('disabled');

    document.getElementById('addForm')
        .addEventListener('submit', addNewCatcher);
}

async function loadCatches() {
    let response = await fetch('http://localhost:3030/data/catches');
    let data = await response.json();

    catchesDiv.innerHTML = '';
    data.forEach(obj => createCatchDOM(obj));
}

async function addNewCatcher(e) {
    e.preventDefault();

    if (authToken === null)
        return alert('Unauthorized action!');

    let formData = new FormData(e.target);
    const angler = formData.get('angler');
    const weight = formData.get('weight');
    const species = formData.get('species');
    const location = formData.get('location');
    const bait = formData.get('bait');
    const captureTime = formData.get('captureTime');

    if (!angler || !weight || !species || !location || !bait || !captureTime)
        return alert('Invalid form!');

    let response = await fetch ('http://localhost:3030/data/catches ', {
        method: 'POST',
        headers: {'Content-Type': 'application/json', 'X-Authorization': authToken},
        body: JSON.stringify({angler, weight, species, location, bait, captureTime})
    });

    if (response.ok) {
        await loadCatches();
    }
    else {
        return alert('Invalid form!');
    }
    [...document.querySelector('#addForm').children]
        .forEach(ch => ch.value = '');
}

function createCatchDOM(obj) {
    let newDiv = document.createElement('div');
    newDiv.className = 'catch';
    newDiv.innerHTML = `<label>Angler</label>
                    <input type="text" class="angler" value="${obj.angler}" />
                    <hr>
                    <label>Weight</label>
                    <input type="number" class="weight" value="${obj.weight}" />
                    <hr>
                    <label>Species</label>
                    <input type="text" class="species" value="${obj.species}" />
                    <hr>
                    <label>Location</label>
                    <input type="text" class="location" value="${obj.location}" />
                    <hr>
                    <label>Bait</label>
                    <input type="text" class="bait" value="${obj.bait}" />
                    <hr>
                    <label>Capture Time</label>
                    <input type="number" class="captureTime" value="${obj.captureTime}" />
                    <hr>`;

    let updateButton = document.createElement('button');
    updateButton.className = 'update';
    updateButton.textContent = 'Update'
    let deleteButton = document.createElement('button');
    deleteButton.className = 'delete';
    deleteButton.textContent = 'Delete'

    if (obj._ownerId === userId) {
        updateButton.addEventListener('click', () => updateCatch(newDiv, obj, obj._id));
        deleteButton.addEventListener('click', () => removeCatch(obj, obj._id));

    }
    else {
        updateButton.disabled = 'true';
        deleteButton.disabled = 'true';
    }

    newDiv.appendChild(updateButton);
    newDiv.appendChild(deleteButton);
    catchesDiv.appendChild(newDiv);
}

async function updateCatch(DOMObj, obj, id) {
    const angler = DOMObj.querySelector('.angler').value;
    const weight = DOMObj.querySelector('.weight').value;
    const species = DOMObj.querySelector('.species').value;
    const location = DOMObj.querySelector('.location').value;
    const bait = DOMObj.querySelector('.bait').value;
    const captureTime = DOMObj.querySelector('.captureTime').value;

    if (obj._ownerId !== userId)
        return alert('Unauthorized action.');

    let response = await fetch(`http://localhost:3030/data/catches/${id}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json', 'X-Authorization': authToken},
        body: JSON.stringify({angler, weight, species, location, bait, captureTime})
    });

    await loadCatches();
}

async function removeCatch(obj, id) {
    if (obj._ownerId !== userId)
        return alert('Suspicious operation.');

    let response = await fetch(`http://localhost:3030/data/catches/${id}`, {
        method: 'DELETE',
        headers: {'Content-Type': 'application/json', 'X-Authorization': authToken}
    });
    await loadCatches();
}