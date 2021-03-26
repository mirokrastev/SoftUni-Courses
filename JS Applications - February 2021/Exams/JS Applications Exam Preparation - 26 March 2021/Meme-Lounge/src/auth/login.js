import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import apiReq from "../api/request.js";
import {setupNavbar} from "../navbar.js";
import {clearNotification, makeNotification} from "../notification.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder() {
    return html`
        <section id="login">
            <form @submit="${loginUser}" id="login-form">
                <div class="container">
                    <h1>Login</h1>
                    <label for="email">Email</label>
                    <input id="email" placeholder="Enter Email" name="email" type="text">
                    <label for="password">Password</label>
                    <input id="password" type="password" placeholder="Enter Password" name="password">
                    <input type="submit" class="registerbtn button" value="Login">
                    <div class="container signin">
                        <p>Dont have an account?<a href="/register">Sign up</a>.</p>
                    </div>
                </div>
            </form>
        </section>`;
}

export function loginView() {
    setupNavbar();
    clearNotification();

    const template = templateBuilder();
    render(template, main);
}

async function loginUser(e) {
    e.preventDefault();
    clearNotification();

    const formData = new FormData(e.target);

    try {
        const result = await api.login(formData);
        page.redirect('/');
    }
    catch (e) {
        makeNotification(e.message);
    }
}