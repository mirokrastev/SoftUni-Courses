import {html, render} from 'https://unpkg.com/lit-html?module';
import {setupNavbar} from "../navbar.js";
import {createTemplate} from "./home.js";
import {checkAuth} from "../auth/checkAuth.js";

const main = document.getElementById('main');
const additional = document.getElementById('additional');

export async function publicationsView() {
    setupNavbar('/my-furniture');
    checkAuth();

    const userId = sessionStorage.getItem('userId');

    const additionalTemplate = html`<h1>Furniture Details</h1>`;
    render(additionalTemplate, additional);

    const data = await (await fetch(`http://localhost:3030/data/catalog?where=_ownerId%3D%22${userId}%22`)).json();

    const template = html`
        <div class="row space-top">
            ${data.map(createTemplate)}
        </div>`;
    render(template, main);
}