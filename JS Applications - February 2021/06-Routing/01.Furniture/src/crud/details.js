import {html, render} from 'https://unpkg.com/lit-html?module';
import {setupNavbar} from "../navbar.js";
import {deleteObject} from "./delete.js";

const main = document.getElementById('main');
const additional = document.getElementById('additional');

function templateBuilder(object) {
    return html`
        <div class="row space-top">
            <div class="col-md-4">
                <div class="card text-white bg-primary">
                    <div class="card-body">
                        <img src="${object.img}"/>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <p>Make: <span>${object.make}</span></p>
                <p>Model: <span>${object.model}</span></p>
                <p>Year: <span>${object.year}</span></p>
                <p>Description: <span>${object.description}</span></p>
                <p>Price: <span>${object.price}</span></p>
                <p>Material: <span>${object.material}</span></p>
                ${checkAuthorization(object)}
            </div>
        </div>`
}

export async function detailsView(ctx) {
    setupNavbar('none');
    const objId = ctx.params.id;
    const object = await (await fetch(`http://localhost:3030/data/catalog/${objId}`)).json()

    const additionalTemplate = html`<h1>Furniture Details</h1>`;
    render(additionalTemplate, additional);

    const template = templateBuilder(object);
    render(template, main);
}

function checkAuthorization(object) {
    const userId = sessionStorage.getItem('userId');

    if (object._ownerId === userId) {
        return html`
            <div>
                <a href="/edit/${object._id}" class="btn btn-info">Edit</a>
                <a @click="${() => deleteObject(object)}" class="btn btn-red">Delete</a>
            </div>`;
        }

    return html``;
}