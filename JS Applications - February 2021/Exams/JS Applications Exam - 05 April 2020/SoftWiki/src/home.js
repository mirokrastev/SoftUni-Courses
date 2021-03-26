import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import apiReq from './api/request.js'
import {setupNavbar} from "./navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateGuestBuilder() {
    return html`
    `;
}

function helperTemplate(e) {
    return html`
        <article>
            <h3>${e.title}</h3>
            <p>${e.content}</p>
            <a href="/details/${e._id}" class="btn details-btn">Details</a>
        </article>`
}

function templateUserBuilder(objects) {
    return html`
        <div class="content">
            <section class="js">
                <h2>JavaScript</h2>
                <div class="articles">
                ${(() => {
                    const jsFilter = objects.filter(e => e.category.toLowerCase() === 'javascript');
                    if (jsFilter.length === 0)
                        return html`<h3 class="no-articles">No articles yet</h3>`;
                    return jsFilter.map(helperTemplate)
                })()}
                </div>
            </section>
            <section class="CSharp">
                <h2>C#</h2>
                <div class="articles">
                    ${(() => {
                        const cSharpFilter = objects.filter(e => e.category.toLowerCase() === 'c#');
                        if (cSharpFilter.length === 0)
                            return html`<h3 class="no-articles">No articles yet</h3>`;
                        return cSharpFilter.map(helperTemplate)
                    })()}
                </div>
            </section>
            <section class="Java">
                <h2>Java</h2>
                <div class="articles">
                    ${(() => {
                        const javaFilter = objects.filter(e => e.category.toLowerCase() === 'java');
                        if (javaFilter.length === 0)
                            return html`<h3 class="no-articles">No articles yet</h3>`;
                        return javaFilter.map(helperTemplate)
                    })()}
                </div>
            </section>
            <section class="Python">
                <h2>Python</h2>
                <div class="articles">
                    ${(() => {
                        const pythonFilter = objects.filter(e => e.category.toLowerCase() === 'python');
                        if (pythonFilter.length === 0)
                            return html`<h3 class="no-articles">No articles yet</h3>`;
                        return pythonFilter.map(helperTemplate)
                    })()}
                </div>
            </section>
        </div>`;
}

export async function homeView() {
    setupNavbar();

    const authToken = sessionStorage.getItem('authToken');
    let template;

    if (authToken) {
        let objects = await api.get('data/articles?sortBy=title desc');
        console.log(objects)
        template = templateUserBuilder(objects);
    }
    else {
        template = templateUserBuilder([]);
    }

    render(template, main);
}