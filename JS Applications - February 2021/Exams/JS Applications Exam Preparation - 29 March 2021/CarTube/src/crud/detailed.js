import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";
import {deleteFunc} from "./delete.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder(object) {
    return html`
        <section id="listing-details">
            <h1>Details</h1>
            <div class="details-info">
                <img src="${object.imageUrl}">
                <hr>
                <ul class="listing-props">
                    <li><span>Brand:</span>${object.brand}</li>
                    <li><span>Model:</span>${object.model}</li>
                    <li><span>Year:</span>${object.year}</li>
                    <li><span>Price:</span>${object.price}$</li>
                </ul>

                <p class="description-para">${object.description}</p>
                ${checkAuth(object)}
            </div>
        </section>`;
}

export async function detailedView(ctx) {
    setupNavbar();

    const id = ctx.params.id;
    try {
        const object = await api.get('data/cars/' + id);
        // fetch here other objects and pass it to the Builder. DO NOT USE async, because it will be shown as
        // [object Promise] in the HTML!
        
        const template = templateBuilder(object);
        render(template, main);
    } catch (e) {
        return alert(e.message);
    }
}

function checkAuth(object) {
    const userId = sessionStorage.getItem('userId');

    if (object._ownerId === userId) {
        return html`
            <div class="listings-buttons">
                <a href="/edit/${object._id}" class="button-list">Edit</a>
                <a @click="${async () => await deleteFunc(object._id)}" href="javascript:void(0)" class="button-list">Delete</a>
            </div>
        `;
    }

    return html`
    `;
}