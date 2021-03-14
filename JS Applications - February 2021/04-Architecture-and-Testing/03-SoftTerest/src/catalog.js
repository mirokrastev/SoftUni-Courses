import {html, render} from 'https://unpkg.com/lit-html?module';

const section = document.getElementById('page');

async function getIdeas() {
    return await (await fetch('http://localhost:3030/data/ideas?select=_id%2Ctitle%2Cimg&sortBy=_createdOn%20desc'))
        .json()
}

export async function setupCatalog() {
    const authToken = sessionStorage.getItem('authToken');
    const data = await getIdeas();
    let template;

    if (data.length === 0) {
        template = html`
        <div id="dashboard-holder">
        <h1>No ideas yet! Be the first one :)</h1>
        </div>`;
    }
    else {
        template = html`
            <div id="dashboard-holder">
            ${data.map(e => html`
                <div class="card overflow-hidden current-card details" style="width: 20rem; height: 18rem;">
                    <div class="card-body">
                        <p class="card-text">${e.title}</p>
                    </div>
                    <img class="card-image" src="${e.img}" alt="Card image cap">
                    ${checkConditions(e._id)}
                </div>`)}
            </div>`;
    }
    render(template, section);
}

function checkConditions(id) {
    return html`<a @click="${async e => {
        await detailedIdea(e, id);
    }}" class="btn" href="">Details</a>`
}

async function detailedIdea(ev, id) {
    ev.preventDefault();
    const data = await (await fetch(`http://localhost:3030/data/ideas/${id}`)).json();
    const userId = sessionStorage.getItem('userId');
    const authToken = sessionStorage.getItem('authToken');

    const template = html`
        <div class="container home some">
            <img class="det-img" src="${data.img}"/>
            <div class="desc">
                <h2 class="display-5">${data.title}</h2>
                <p class="infoType">Description:</p>
                <p class="idea-description">${data.description}</p>
            </div>
            ${await checkConditions()}
        </div>`;

    async function checkConditions() {
        if (data._ownerId === userId) {
            return html`
                <div class="text-center">
                    <a @click="${async (e) => {
                        e.preventDefault();
                        await deleteIdea(data._id, authToken);
                    }}" class="btn detb" href="">Delete</a>
                </div>`
        }
        return html``;
    }

    render(template, section);
}

async function deleteIdea(id, authToken) {
    await fetch(`http://localhost:3030/data/ideas/${id}`, {
        method: 'DELETE',
        headers: {'X-Authorization': authToken}
    });
    return setupCatalog();
}