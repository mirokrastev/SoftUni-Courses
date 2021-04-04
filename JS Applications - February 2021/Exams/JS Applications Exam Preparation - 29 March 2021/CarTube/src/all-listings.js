import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import apiReq from './api/request.js'
import {setupNavbar} from "./navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder(objects) {
    if (objects.length === 0) {
        return html`
            <section id="car-listings">
                <h1>Car Listings</h1>
                <div class="listings">
                    <p class="no-cars">No cars in database.</p>
                </div>
            </section>`;
    }

    return html`
        <section id="car-listings">
            <h1>Car Listings</h1>
            <div class="listings">
                ${objects.map(e => html`
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

export async function allListingsView() {
    setupNavbar();

    const object = await api.get('data/cars?sortBy=_createdOn%20desc');
    const template = templateBuilder(object);

    render(template, main);
}