import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";
import {deleteFunc} from "./delete.js";
import {clearNotification} from "../notification.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder(object) {
    return html`
        <section id="meme-details">
            <h1>Meme Title: ${object.title}

            </h1>
            <div class="meme-details">
                <div class="meme-img">
                    <img alt="meme-alt" src="${object.imageUrl}">
                </div>
                <div class="meme-description">
                    <h2>Meme Description</h2>
                    <p>
                        ${object.description}
                    </p>
                    
                    ${checkAuth(object)}
                </div>
            </div>
        </section>`;
}

export async function detailedView(ctx) {
    setupNavbar();
    clearNotification();

    const id = ctx.params.id;
    try {
        const object = await api.get('data/memes/' + id);
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
            <a class="button warning" href="/edit/${object._id}">Edit</a>
            <button @click="${async () => await deleteFunc(object._id)}" class="button danger">Delete</button>`;
    }

    return html`
    `;
}