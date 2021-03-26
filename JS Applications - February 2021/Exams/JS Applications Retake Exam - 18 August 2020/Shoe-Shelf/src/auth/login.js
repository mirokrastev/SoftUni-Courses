import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder() {
    return html`
        <h1>Login</h1>
        <p class="form-info">Don't have account?
            <a href="/register">Register now</a> and fix that!
        </p>
        <form @submit="${loginUser}">
            <div>
                <input type="email" name="email" placeholder="Email...">
            </div>

            <div>
                <input type="password" name="password" placeholder="Password...">
            </div>
            <div>
                <button>Login</button>
            </div>
        </form>`;
}

export function loginView() {
    setupNavbar();

    const template = templateBuilder();
    render(template, main);
}

async function loginUser(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    try {
        const result = await api.login(formData);
        page.redirect('/');
    }
    catch (e) {
        return alert(e);
    }
}