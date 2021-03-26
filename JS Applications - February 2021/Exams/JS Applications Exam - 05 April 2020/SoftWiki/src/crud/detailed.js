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
        <div class="container details">
            <div class="details-content">
                <h2>${object.title}</h2>
                <strong>${object.category}</strong>
                <p>${object.content}</p>
                ${checkAuth(object)}
            </div>
        </div>`;
}

export async function detailedView(ctx) {
    setupNavbar();

    const id = ctx.params.id;
    try {
        const object = await api.get('data/articles/' + id, true);
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
            <div class="buttons">
                <a @click="${async () => await deleteFunc(object._id)}" href="javascript:void(0)" class="btn delete">Delete</a>
                <a href="/edit/${object._id}" class="btn edit">Edit</a>
            </div>`;
    }

    return html`
        <div class="buttons">
            <a href="/" class="btn edit">Back</a>
        </div>`;
}