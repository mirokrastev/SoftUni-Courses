import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";
import {clearNotification, makeNotification} from "../notification.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder() {
    return html`
        <section id="create-meme">
            <form @submit="${createFunc}" id="create-form">
                <div class="container">
                    <h1>Create Meme</h1>
                    <label for="title">Title</label>
                    <input id="title" type="text" placeholder="Enter Title" name="title">
                    <label for="description">Description</label>
                    <textarea id="description" placeholder="Enter Description" name="description"></textarea>
                    <label for="imageUrl">Meme Image</label>
                    <input id="imageUrl" type="text" placeholder="Enter meme ImageUrl" name="imageUrl">
                    <input type="submit" class="registerbtn button" value="Create Meme">
                </div>
            </form>
        </section>`;
}

export function createView() {
    setupNavbar();
    clearNotification();

    const template = templateBuilder();
    render(template, main);
}

async function createFunc(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const data = FormDataPairs(formData);

    if (!data['title'] || !data['description'] || !data['imageUrl']) {
        return makeNotification('Invalid form');
    }

    try {
        const result = await api.post('data/memes', data, true);
        page.redirect('/all-memes');
    }
    catch (e) {
        makeNotification(e.message);
    }
}