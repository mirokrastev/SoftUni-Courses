import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder() {
    return html`
        <h1>Create New Offer</h1>
        <p class="message"></p>
        <form @submit="${createFunc}">
            <div>
                <input type="text" name="name" placeholder="Name...">
            </div>
            <div>
                <input type="text" name="price" placeholder="Price...">
            </div>
            <div>
                <input type="text" name="imageUrl" placeholder="Image url...">
            </div>
            <div>
                <textarea name="description" placeholder="Give us some description about this offer..."></textarea>
            </div>
            <div>
                <input name="brand" type="text" placeholder="Brand...">
            </div>
            <div>
                <button>Create</button>
            </div>
        </form>`;
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
    data['people'] = [];
    // form validation length, etc..

    try {
        const result = await api.post('data/shoes', data, true);
        page.redirect('/');
    }
    catch (e) {
        return alert(e.message);
    }
}