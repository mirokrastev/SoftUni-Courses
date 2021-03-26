import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder() {
    return html`
        <div class="container">
            <form @submit="${createFunc}">
                <fieldset>
                    <legend>Create article</legend>
                    <p class="field title">
                        <input type="text" id="title" name="title" placeholder="Arrays">
                        <label for="title">Title:</label>
                    </p>

                    <p class="field category">
                        <input type="text" id="category" name="category" placeholder="JavaScript">
                        <label for="category">Category:</label>
                    </p>
                    <p class="field content">
                        <textarea name="content" id="content"></textarea>
                        <label for="content">Content:</label>
                    </p>

                    <p class="field submit">
                        <button class="btn submit" type="submit">Create</button>
                    </p>

                </fieldset>
            </form>
        </div>`;
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

    // form validation length, etc..

    try {
        const result = await api.post('data/articles', data, true);
        page.redirect('/');
    }
    catch (e) {
        return alert(e.message);
    }
}