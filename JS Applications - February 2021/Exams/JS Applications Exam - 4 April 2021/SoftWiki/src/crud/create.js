import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder() {
    return html`
        <section id="create-page" class="content">
            <h1>Create Article</h1>

            <form id="create" @submit="${createFunc}">
                <fieldset>
                    <p class="field title">
                        <label for="create-title">Title:</label>
                        <input type="text" id="create-title" name="title" placeholder="Enter article title">
                    </p>

                    <p class="field category">
                        <label for="create-category">Category:</label>
                        <input type="text" id="create-category" name="category" placeholder="Enter article category">
                    </p>
                    <p class="field">
                        <label for="create-content">Content:</label>
                        <textarea name="content" id="create-content"></textarea>
                    </p>

                    <p class="field submit">
                        <input class="btn submit" type="submit" value="Create">
                    </p>

                </fieldset>
            </form>
        </section>`;
}

export function createView() {
    setupNavbar();
    
    const template = templateBuilder();
    render(template, main);
}

async function createFunc(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const data = FormDataPairs(formData);

    if (!data['title'] || !data['content'] || !data['category'])
        return alert('Invalid form.');

    if (!['JavaScript', 'C#', 'Java', 'Python'].find(e => e === data['category']))
        return alert('Invalid category!');

    try {
        const result = await api.post('data/wiki', data, true);
        page.redirect('/');
    }
    catch (e) {
        return alert(e.message);
    }
}