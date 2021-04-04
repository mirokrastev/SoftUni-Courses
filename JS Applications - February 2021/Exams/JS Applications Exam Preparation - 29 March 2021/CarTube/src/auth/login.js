import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import apiReq from "../api/request.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder() {
    return html`
        <section id="login">
            <div class="container">
                <form @submit="${loginUser}" id="login-form">
                    <h1>Login</h1>
                    <p>Please enter your credentials.</p>
                    <hr>

                    <p>Username</p>
                    <input placeholder="Enter Username" name="username" type="text">

                    <p>Password</p>
                    <input type="password" placeholder="Enter Password" name="password">
                    <input type="submit" class="registerbtn" value="Login">
                </form>
                <div class="signin">
                    <p>Dont have an account?
                        <a href="/register">Sign up</a>.
                    </p>
                </div>
            </div>
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
        page.redirect('/all-listings');
    }
    catch (e) {
        return alert(e);
    }
}