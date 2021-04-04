import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import apiReq from './api/request.js'
import {setupNavbar} from "./navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function objectTemplateBuilder(object) {
    if (object.length === 0) {
        return html`
            <h2>Results:</h2>
            <div class="listings">
                <p class="no-cars"> No results.</p>
            </div>`;
    }
    return html`
        <h2>Results:</h2>
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
        </div>`;
}

function mainTemplateBuilder() {
    return html`
        <section id="search-cars">
            <h1>Filter by year</h1>

            <div class="container">
                <input type="text" id="search-input" name="search" placeholder="Enter desired production year">
                <button @click="${() => {
                    const id = Number(document.getElementById('search-input').value);
                    page.redirect('/search?q='+id);
                }}" class="button-list">Search</button>
            </div>
            
            <div id="results">
                
            </div>
        </section>`
}

export async function searchListingsView(ctx) {
    const query = Number(ctx.querystring.split('=')[1]);
    if (Number.isNaN(query)) {
        const template = mainTemplateBuilder();
        render(template, main);
    }
    else {
        const object = await api.get(`data/cars?where=year%3D${query}`);
        const template = objectTemplateBuilder(object);
        const newMain = document.getElementById('results');
        render(template, newMain);
    }
}