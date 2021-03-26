import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder() {
    return html`
        <div class="container auth">
            <form @submit="${registerUser}">
                <fieldset>
                    <legend>Register</legend>
                    <blockquote>Knowledge is not simply another commodity. On the contrary. Knowledge is never used up. It increases by diffusion and grows by dispersion.</blockquote>
                    <p class="field email">
                        <input type="email" id="email" name="email" placeholder="maria@email.com">
                        <label for="email">Email:</label>
                    </p>
                    <p class="field password">
                        <input type="password" name="password" id="register-pass">
                        <label for="register-pass">Password:</label>
                    </p>
                    <p class="field password">
                        <input type="password" name="rePass" id="rep-pass">
                        <label for="rep-pass">Repeat password:</label>
                    </p>
                    <p class="field submit">
                        <button class="btn submit" type="submit">Register</button>
                    </p>
                    <p class="field">
                        <span>If you already have profile click <a href="/login">here</a></span>
                    </p>
                </fieldset>
            </form>
        </div>`;
}

export function registerView() {
    setupNavbar();

    const template = templateBuilder();
    render(template, main);
}

async function registerUser(e) {
    e.preventDefault();

    const formData = new FormData(e.target);

    try {
        const result = await api.register(formData);
        page.redirect('/')
    }
    catch (e) {
        return alert(e.message);
    }
}