import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import apiReq from './api/request.js'
import {setupNavbar} from "./navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder(object) {
    if (object.length === 0) {
        return html`
            <section id="my-listings">
                <h1>My car listings</h1>
                <div class="listings">
                    <p class="no-cars"> You haven't listed any cars yet.</p>
                </div>
            </section>`;
    }
    return html`
        <section id="my-listings">
            <h1>My car listings</h1>
            <div class="listings">
                ${object.map(e => html`
                    <div class="listing">
                        <div class="preview">
                            <img src="${e.imageUrl}">
                        </div>
                        <h2>${e.brand} ${e.model}</h2>
                        <div class="info">
                            <div class="data-info">
                                <h3>Year: ${e.year}</h3>
                                <h3>Price: ${e.price} $</h3>
                            </div>
                            <div class="data-buttons">
                                <a href="/details/${e._id}" class="button-carDetails">Details</a>
                            </div>
                        </div>
                    </div>`)}
            </div>
        </section>`;
}

export async function myListingsView() {
    setupNavbar();

    const userId = sessionStorage.getItem('userId');
    const objects = await api.get(`data/cars?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`);
    const template = templateBuilder(objects);

    render(template, main);
}