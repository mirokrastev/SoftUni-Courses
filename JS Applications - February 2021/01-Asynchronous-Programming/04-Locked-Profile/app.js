let lastUser = 1;
const mainEl = document.getElementById('main');

function lockedProfile() {
    Array.from(mainEl.children)
        .forEach(e => e.remove());
    fetch('http://localhost:3030/jsonstore/advanced/profiles')
        .then(response => response.json())
        .then(data => {
            Object.values(data)
                .forEach(e => makeProfile(e));
        });
}

// factory function for creating a profile.
function makeProfile(object) {
    if (lastUser > 3) {
        lastUser = 1;
    }
    let newProfileDiv = document.createElement('div');
    newProfileDiv.className = 'profile';
    newProfileDiv.innerHTML += `
        <img src="./iconProfile2.png"/>
        <label>Lock</label>
        <input type="radio" name="user${lastUser}Locked" value="lock">
        <label>Unlock</label>
        <input type="radio" name="user${lastUser}Locked" value="unlock">
        <hr>
        <label>Username</label>
        <input type="text" name="user${lastUser}Username" value="${object.username}" disabled readonly/>
        <div id="user${lastUser}HiddenFields">
            <hr>
            <label>Email:</label>
            <input type="email" name="user${lastUser}Email" value="${object.email}" disabled readonly/>
            <label>Age:</label>
            <input type="email" name="user${lastUser}Age" value="31" disabled readonly>
        </div>`;

    let showMoreButton = document.createElement('button');
    showMoreButton.textContent = 'Show more';
    showMoreButton.addEventListener('click', () => showMore(newProfileDiv));
    newProfileDiv.appendChild(showMoreButton);

    mainEl.appendChild(newProfileDiv);

    lastUser++;
}

function showMore(profile) {
    let allRadioButtons = Array.from(profile.querySelectorAll('input')).slice(0, 2);
    if (allRadioButtons[0].checked || (!allRadioButtons[0].checked && !allRadioButtons[1].checked))
        return;

    const button = profile.querySelector('button');
    const div = profile.querySelector('div')

    if (button.textContent === 'Show less') {
        button.textContent = 'Show more';
        div.style.display = 'none';
        return;
    }
    button.textContent = 'Show less';
    div.style.display = 'block';
}