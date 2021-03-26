import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder() {
    return html`
        <h1>Register</h1>
        <p class="form-info">Already registered?
            <a href="/login">Login now</a> and have some fun!
        </p>

        <form @submit="${registerUser}">
            <div>
                <input type="email" name="email" placeholder="Email...">
            </div>
            <div>
                <input type="password" name="password" placeholder="Password">
            </div>
            <div>
                <input type="password" name="rePass" placeholder="Re-password">
            </div>
            <div>
                <p class="message"></p>
                <button>Register</button>
            </div>
        </form>`;
}

export function registerView() {
    const template = templateBuilder();
    render(template, main);
}

async function registerUser(e) {
    e.preventDefault();

    const formData = new FormData(e.target);

    try {
        const result = await api.register(formData);
        sessionStorage.setItem('userEmail', result.email);
        page.redirect('/')
    }
    catch (e) {
        return alert(e.message);
    }
}