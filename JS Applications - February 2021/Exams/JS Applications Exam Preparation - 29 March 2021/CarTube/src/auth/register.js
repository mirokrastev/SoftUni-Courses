import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder() {
    return html`
        <section id="register">
            <div class="container">
                <form @submit="${registerUser}" id="register-form">
                    <h1>Register</h1>
                    <p>Please fill in this form to create an account.</p>
                    <hr>

                    <p>Username</p>
                    <input type="text" placeholder="Enter Username" name="username" required>

                    <p>Password</p>
                    <input type="password" placeholder="Enter Password" name="password" required>

                    <p>Repeat Password</p>
                    <input type="password" placeholder="Repeat Password" name="repeatPass" required>
                    <hr>

                    <input type="submit" class="registerbtn" value="Register">
                </form>
                <div class="signin">
                    <p>Already have an account?
                        <a href="/login">Sign in</a>.
                    </p>
                </div>
            </div>
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
        page.redirect('/all-listings')
    }
    catch (e) {
        return alert(e.message);
    }
}