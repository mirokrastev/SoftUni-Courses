import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder() {
    return html`
        <section id="register-page" class="content auth">
            <h1>Register</h1>

            <form id="register" @submit="${registerUser}">
                <fieldset>
                    <blockquote>Knowledge is not simply another commodity. On the contrary. Knowledge is never used up.
                        It
                        increases by diffusion and grows by dispersion.</blockquote>
                    <p class="field email">
                        <label for="register-email">Email:</label>
                        <input type="email" id="register-email" name="email" placeholder="maria@email.com">
                    </p>
                    <p class="field password">
                        <label for="register-pass">Password:</label>
                        <input type="password" name="password" id="register-pass">
                    </p>
                    <p class="field password">
                        <label for="register-rep-pass">Repeat password:</label>
                        <input type="password" name="rep-pass" id="register-rep-pass">
                    </p>
                    <p class="field submit">
                        <input class="btn submit" type="submit" value="Register">
                    </p>
                    <p class="field">
                        <span>If you already have profile click <a href="/login">here</a></span>
                    </p>
                </fieldset>
            </form>
        </section>`;
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