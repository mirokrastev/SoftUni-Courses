import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import {setupNavbar} from "./navbar.js";
import apiReq from "./api/request.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateGuestBuilder() {
    return html`
        <div class="container">
            <div class="about-us">
                <div>
                    <img src="../public/shoes.jpg" alt="">
                    <img src="../public/shoes2.jpg" alt="">
                </div>
                <p>
                    <a href="/register">Register Now</a> and Try it!
                </p>
            </div>
        </div>`;
}

function templateUsersBuilder(object) {
    if (object && object.length > 0) {
        return html`
            <div class="shoes">
                ${object.map(e => html`
                    <div class="shoe" @click="${() => {
                        page.redirect(`/details/${e._id}`)
                    }}">
                        <img src="${e.imageUrl}">
                        <h3>${e.name}</h3>
                        <a>Buy it for $${e.price}</a>
                    </div>
                `)}
            </div>`;
    }
    return html`
    <div class="shoes">
        No shoes to display. Be the first to create a new offer...
    </div>`;
}

export async function homeView() {
    setupNavbar();
    let template;
    const authToken = sessionStorage.getItem('authToken');

    if (authToken) {
        let objects;
        try {
            objects = await api.get('data/shoes');
        }
        catch (e) {
            objects = null;
        }

        template = templateUsersBuilder(objects);
    }
    else {
        template = templateGuestBuilder();
    }

    render(template, main);
}