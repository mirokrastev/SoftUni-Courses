import {html, render} from 'https://unpkg.com/lit-html?module';
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('main');
const additional = document.getElementById('additional');

export function createTemplate(e) {
    return html`
                <div class="col-md-4">
                    <div class="card text-white bg-primary">
                        <div class="card-body">
                            <img src="${e.img}"/>
                            <p>${e.description}</p>
                            <footer>
                                <p>Price: <span>${e.price} $</span></p>
                            </footer>
                            <div>
                                <a href="/details/${e._id}" class="btn btn-info">Details</a>
                            </div>
                        </div>
                    </div>`
}

export async function homeView() {
    setupNavbar('/');
    const additionalTemplate = html`
        <h1>Welcome to Furniture System</h1>
        <p>Select furniture from the catalog to view details.</p>`;
    render(additionalTemplate, additional);

    let data = await (await fetch('http://localhost:3030/data/catalog')).json();
    const template = html`
        <div class="row space-top">
            ${data.map(createTemplate)}
                </div>`;
    render(template, main);
}