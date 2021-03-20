import {html, render} from 'https://unpkg.com/lit-html?module';
import page from "//unpkg.com/page/page.mjs";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('main');
const additional = document.getElementById('additional');

function templateBuilder() {
    return html`
        <form @submit=${registerUser}>
            <div class="row space-top">
                <div class="col-md-4">
                    <div class="form-group">
                        <label class="form-control-label" for="email">Email</label>
                        <input class="form-control" id="email" type="text" name="email">
                    </div>
                    <div class="form-group">
                        <label class="form-control-label" for="password">Password</label>
                        <input class="form-control" id="password" type="password" name="password">
                    </div>
                    <div class="form-group">
                        <label class="form-control-label" for="rePass">Repeat</label>
                        <input class="form-control" id="rePass" type="password" name="rePass">
                    </div>
                    <input type="submit" class="btn btn-primary" value="Register" />
                </div>
            </div>
        </form>`
}

export function registerView() {
    setupNavbar('/register');
    const additionalTemplate = html`<h1>Register New User</h1><p>Please fill all fields.</p>`;
    render(additionalTemplate, additional);

    const template = templateBuilder();
    render(template, main);
}

async function registerUser(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const email = formData.get('email');
    const password = formData.get('password');
    const rePass = formData.get('rePass');

    if (password !== rePass) {
        return alert('Passwords doesn\'t match!');
    }

    const response = await fetch('http://localhost:3030/users/register', {
        method: 'POST',
        body: JSON.stringify({email, password})
    });

    if (!response.ok) {
        return alert('Invalid form.');
    }
    const data = await response.json();
    sessionStorage.setItem('authToken', data.accessToken);
    sessionStorage.setItem('userId', data._id);

    page.redirect('/');
}