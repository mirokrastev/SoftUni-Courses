import {html, render} from 'https://unpkg.com/lit-html?module';
import {logoutUser} from "./auth/logout.js";

const navbar = document.getElementById('navbar');

const mapper = {
    '/': 'catalogLink',
    '/login':'loginLink',
    '/register': 'registerLink',
    '/create': 'createLink',
    '/my-furniture': 'publicationLink'
}

export function setupNavbar(currentPath) {
    const authToken = sessionStorage.getItem('authToken');
    let template;

    if (authToken === null) {
        template = html`
            <a id="catalogLink" href="/">Dashboard</a>
            <div id="guest">
                <a id="loginLink" href="/login">Login</a>
                <a id="registerLink" href="/register">Register</a>
            </div>`;
    }
    else {
        template = html`
            <a id="catalogLink" href="/">Dashboard</a>
            <div id="user">
                <a id="createLink" href="/create" >Create Furniture</a>
                <a id="publicationLink" href="/my-furniture">My Publications</a>
                <a @click=${logoutUser} id="logoutBtn" href="javascript:void(0)">Logout</a>
            </div>`;
    }

    render(template, navbar);

    if (!mapper.hasOwnProperty(currentPath)) {
        currentPath = 'none';
    }

    changeNavLinks(currentPath)
}

function changeNavLinks(currentPath) {
    Object.values(mapper)
        .forEach(key => {
            const el = document.getElementById(key);
            if (!el)
                return;
            el.className = '';
        });

    if (currentPath === 'none')
        return;
    try {
        document.getElementById(mapper[currentPath]).className = 'active';
    }
    catch (err) {
    }
}