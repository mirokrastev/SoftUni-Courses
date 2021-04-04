import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import apiReq from "../api/request.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder() {
    return html`
        <section id="login-page" class="content auth">
            <h1>Login</h1>

            <form id="login" @submit="${loginUser}">
                <fieldset>
                    <blockquote>Knowledge is like money: to be of value it must circulate, and in circulating it can
                        increase in quantity and, hopefully, in value</blockquote>
                    <p class="field email">
                        <label for="email">Email:</label>
                        <input type="email" id="email" name="email" placeholder="maria@email.com">
                    </p>
                    <p class="field password">
                        <label for="login-pass">Password:</label>
                        <input type="password" id="login-pass" name="password">
                    </p>
                    <p class="field submit">
                        <input class="btn submit" type="submit" value="Log in">
                    </p>
                    <p class="field">
                        <span>If you don't have profile click <a href="/register">here</a></span>
                    </p>
                </fieldset>
            </form>
        </section>`;
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