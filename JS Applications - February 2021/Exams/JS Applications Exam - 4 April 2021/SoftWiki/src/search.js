import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import apiReq from './api/request.js'
import {setupNavbar} from "./navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function objectTemplateBuilder(object) {
    if (object.length === 0) {
        return html`
            <div class="search-container">
                <h3 class="no-articles">No matching articles</h3>
            </div>`;
    }
    return html`
        <div class="search-container">
        ${object.map(e => html`
            <a class="article-preview" href="/details/${e._id}">
                <article>
                    <h3>Topic: <span>${e.title}</span></h3>
                    <p>Category: <span>${e.category}</span></p>
                </article>
            </a>`)}
        </div>`;
}


function mainTemplateBuilder() {
    return html`
        <section id="search-page" class="content">
            <h1>Search</h1>
            <form @submit="${onFormSubmit}" id="search-form">
                <p class="field search">
                    <input type="text" placeholder="Search by article title" name="search">
                </p>
                <p class="field submit">
                    <input class="btn submit" type="submit" value="Search">
                </p>
            </form>
            <div id="results"></div>
        </section>`;
}

export async function searchTopicView(ctx) {
    const query = ctx.querystring.split('=')[1];

    if (query === '') {
        const template = objectTemplateBuilder([]);
        const newMain = document.getElementById('results');
        return render(template, newMain);
    }

    if (!query) {
        const template = mainTemplateBuilder();
        render(template, main);
    }
    else {
        const object = await api.get(`data/wiki?where=title%20LIKE%20%22${query}%22`);
        const template = objectTemplateBuilder(object);
        const newMain = document.getElementById('results');
        render(template, newMain);
    }
}

async function onFormSubmit(e) {
    e.preventDefault();
    const search = (new FormData(e.target)).get('search');
    page.redirect('/search?q=' + search);
}