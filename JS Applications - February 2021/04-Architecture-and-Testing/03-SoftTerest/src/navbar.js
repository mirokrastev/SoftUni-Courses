import {html, render} from 'https://unpkg.com/lit-html?module';
import {loginView} from './auth/login.js'
import {registerView} from './auth/register.js'
import {logoutView} from "./auth/logout.js";
import {main} from "./app.js";
import {setupCatalog} from "./catalog.js";
import {createView} from "./create.js";

const navbarSection = document.getElementById('navbarResponsive');
document.getElementById('icon')
    .addEventListener('click', e => {
        e.preventDefault()
        return main();
    });

export function setupUserNav() {
    const authToken = sessionStorage.getItem('authToken');

    let navbar;
    if (authToken === null) {
        navbar = html`
        <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a @click="${setupCatalog}" class="nav-link">Dashboard</a>
            </li>
            <li class="nav-item">
            <a @click="${loginView}" class="nav-link">Login</a>
            </li>
            <li class="nav-item">
                <a @click="${registerView}" class="nav-link">Register</a>
            </li>
        </ul>`;
    }
    else {
       navbar = html`
        <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a @click="${setupCatalog}" class="nav-link">Dashboard</a>
            </li>
            <li class="nav-item">
                <a @click="${createView}" class="nav-link">Create</a>
            </li>
            <li class="nav-item">
                <a @click="${logoutView}" class="nav-link">Logout</a>
            </li>
        </ul>`;
    }
    render(navbar, navbarSection);
}