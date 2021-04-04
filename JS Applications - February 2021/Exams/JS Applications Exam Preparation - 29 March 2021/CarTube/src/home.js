import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import apiReq from './api/request.js'
import {setupNavbar} from "./navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateGuestBuilder() {
    return html`
        <section id="main">
            <div id="welcome-container">
                <h1>Welcome To Car Tube</h1>
                <img class="hero" src="/images/car-png.webp" alt="carIntro">
                <h2>To see all the listings click the link below:</h2>
                <div>
                    <a href="/all-listings" class="button">Listings</a>
                </div>
            </div>
        </section>`;
}
 // for pagination include page, pages
function templateUserBuilder(objects) {
    return html`
    `;
}

export async function homeView() {
    setupNavbar();

    const authToken = sessionStorage.getItem('authToken');
    let template;

    if (authToken) {
        template = templateGuestBuilder();
    }
    else {
        template = templateGuestBuilder();
    }

    render(template, main);
}