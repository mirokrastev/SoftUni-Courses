import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import {logoutUser} from "./auth/logout.js";

const main = document.getElementById('navBar');

export function setupNavbar() {
    const authToken = sessionStorage.getItem('authToken');
    let template;

    if (authToken === null) {
        template = html`
            <h1><a class="home" href="/login">SoftWiki</a></h1>
            <nav class="nav-buttons">
                <a href="/register">Register</a>
            </nav>`;
    }
    else {
        template = html`
            <h1><a class="home" href="/">SoftWiki</a></h1>
            <nav class="nav-buttons">
                <a href="/create">Create</a>
                <a @click="${logoutUser}" href="javascript:void(0)">Logout</a>
            </nav>`;
    }

    render(template, main);
}

// if (!mapper.hasOwnProperty(currentPath)) {
//       currentPath = 'none';
//     }

// changeNavLinks(currentPath)


// const mapper = {
//     '/': 'catalogLink',
//     '/login':'loginLink',
//     '/register': 'registerLink',
//     '/create': 'createLink',
//     '/my-furniture': 'publicationLink'
// }

// function changeNavLinks(currentPath) {
//     Object.values(mapper)
//         .forEach(key => {
//             const el = document.getElementById(key);
//             if (!el)
//                 return;
//             el.className = '';
//         });

//     if (currentPath === 'none')
//         return;
//     try {
//         document.getElementById(mapper[currentPath]).className = 'active';
//     }
//     catch (err) {
//     }
// }