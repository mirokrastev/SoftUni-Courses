import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";
import {deleteFunc} from './delete.js';

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder(object) {
    return html`
        <section id="details-page" class="content details">
            <h1>${object.title}</h1>

            <div class="details-content">
                <strong>Published in category ${object.category}</strong>
                <p>${object.content}</p>

                ${checkAuth(object)}
            </div>
        </section>`;
}

export async function detailedView(ctx) {
    setupNavbar();

    const id = ctx.params.id;
    try {
        const object = await api.get('data/wiki/' + id);
        
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
                <a href="javascript:void(0)" @click="${async () => await deleteFunc(object._id)}" class="btn delete">Delete</a>
                <a href="/edit/${object._id}" class="btn edit">Edit</a>
            </div>`;
    }

    return html`
        <div class="buttons">
            <a href="/" class="btn edit">Back</a>
        </div>`;
}