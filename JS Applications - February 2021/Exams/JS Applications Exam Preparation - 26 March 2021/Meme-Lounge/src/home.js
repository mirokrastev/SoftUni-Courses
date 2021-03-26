import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import apiReq from './api/request.js'
import {setupNavbar} from "./navbar.js";
import {clearNotification} from "./notification.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateGuestBuilder() {
    return html`
        <section id="welcome">
            <div id="welcome-container">
                <h1>Welcome To Meme Lounge</h1>
                <img src="/images/welcome-meme.jpg" alt="meme">
                <h2>Login to see our memes right away!</h2>
                <div id="button-div">
                    <a href="/login" class="button">Login</a>
                    <a href="/register" class="button">Register</a>
                </div>
            </div>
        </section>`;
}

function templateUserBuilder(objects) {
    if (objects.length === 0)
        return html`
            <section id="meme-feed">
                <h1>All Memes</h1>
                <div id="memes">
                    <p class="no-memes">No memes in database.</p>
                </div>
            </section>`;

    return html`
        <section id="meme-feed">
            <h1>All Memes</h1>
            <div id="memes">
                ${objects.map(e => html`
                    <div class="meme">
                        <div class="card">
                            <div class="info">
                                <p class="meme-title">${e.title}</p>
                                <img class="meme-image" alt="meme-img" src="${e.imageUrl}">
                            </div>
                            <div id="data-buttons">
                                <a class="button" href="/details/${e._id}">Details</a>
                            </div>
                        </div>
                    </div>`)}
            </div>
        </section>`;
}

export async function homeView() {
    setupNavbar();
    clearNotification();

    const authToken = sessionStorage.getItem('authToken');
    let template;

    if (authToken) {
        return page.redirect('/all-memes');
    }
    else {
        template = templateGuestBuilder();
    }

    render(template, main);
}

export async function allMemesView() {
    setupNavbar();
    clearNotification();

    let objects = await api.get('data/memes?sortBy=_createdOn%20desc');
    const template = templateUserBuilder(objects);

    render(template, main);
}