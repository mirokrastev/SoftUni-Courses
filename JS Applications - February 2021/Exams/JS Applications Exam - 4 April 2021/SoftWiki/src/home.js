import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import apiReq from './api/request.js'
import {setupNavbar} from "./navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateGuestBuilder(object) {
    const jsObj = object.find(e => e.category === 'JavaScript');
    const pyObj = object.find(e => e.category === 'Python');
    const cObj = object.find(e => e.category === 'C#');
    const javaObj = object.find(e => e.category === 'Java');

    return html`
        <section id="home-page" class="content">
            <h1>Recent Articles</h1>
            <section class="recent js">
                <h2>JavaScript</h2>
                ${(() => {
                    if (!jsObj)
                        return html`<h3 class="no-articles">No articles yet</h3>`;
                    return html`
                        <article>
                            <h3>${jsObj.title}</h3>
                            <p>${jsObj.content}</p>
                            <a href="/details/${jsObj._id}" class="btn details-btn">Details</a>
                        </article>`;
                })()}
            </section>
            <section class="recent csharp">
                <h2>C#</h2>
                ${(() => {
                    if (!cObj)
                        return html`<h3 class="no-articles">No articles yet</h3>`;
                    return html`
                        <article>
                            <h3>${cObj.title}</h3>
                            <p>${cObj.content}</p>
                            <a href="/details/${cObj._id}" class="btn details-btn">Details</a>
                        </article>`;
                })()}
            </section>
            <section class="recent java">
                <h2>Java</h2>
                ${(() => {
                    if (!javaObj)
                        return html`<h3 class="no-articles">No articles yet</h3>`;
                    return html`
                        <article>
                            <h3>${javaObj.title}</h3>
                            <p>${javaObj.content}</p>
                            <a href="/details/${javaObj._id}" class="btn details-btn">Details</a>
                        </article>`;
                })()}
            </section>
            <section class="recent python">
                <h2>Python</h2>
                ${(() => {
                    if (!pyObj)
                        return html`<h3 class="no-articles">No articles yet</h3>`;
                    return html`
                        <article>
                            <h3>${pyObj.title}</h3>
                            <p>${pyObj.content}</p>
                            <a href="/details/${pyObj._id}" class="btn details-btn">Details</a>
                        </article>`;
                })()}
            </section>
        </section>`;
}

function templateUserBuilder(objects) {
    if (objects.length === 0) {
        return html`
            <section id="catalog-page" class="content catalogue">
                <h1>All Articles</h1>
                <h3 class="no-articles">No articles yet</h3>
            </section>;`
    }

    return html`
        <section id="catalog-page" class="content catalogue">
            <h1>All Articles</h1>
            ${objects.map(e => html`
                <a class="article-preview" href="/details/${e._id}">
                    <article>
                        <h3>Topic: <span>${e.title}</span></h3>
                        <p>Category: <span>${e.category}</span></p>
                    </article>
                </a>`)}
        </section>`;
}

export async function homeView() {
    setupNavbar();

    const objects = await api.get('data/wiki?sortBy=_createdOn%20desc&distinct=category');
    const template = templateGuestBuilder(objects);

    render(template, main);
}

export async function catalogueView() {
    setupNavbar();

    const objects = await api.get('data/wiki?sortBy=_createdOn%20desc');
    const template = templateUserBuilder(objects);

    render(template, main);
}