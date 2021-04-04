import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import {logoutUser} from "./auth/logout.js";

const main = document.getElementById('navBar');

export function setupNavbar() {
    const authToken = sessionStorage.getItem('authToken');
    let template;

    if (authToken === null) {
        template = html`
            <header>
                <h1><a class="home" href="/">SoftWiki</a></h1>
                <nav class="nav-buttons">
                    <a href="/catalogue">Catalogue</a>
                    <a href="/search">Search</a>
                    <div id="guest">
                        <a href="/login">Login</a>
                        <a href="/register">Register</a>
                    </div>
                </nav>
            </header>`;
    }
    else {
        template = html`
            <header>
                <h1><a class="home" href="/">SoftWiki</a></h1>
                <nav class="nav-buttons">
                    <a href="/catalogue">Catalogue</a>
                    <a href="/search">Search</a>
                    <div id="user">
                        <a href="/create">Create</a>
                        <a href="javascript:void(0)" @click="${logoutUser}">Logout</a>
                    </div>
                </nav>
            </header>`;
    }

    render(template, main);
}