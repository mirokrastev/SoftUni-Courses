import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import {logoutUser} from "./auth/logout.js";

const main = document.getElementById('navBar');

export function setupNavbar() {
    const authToken = sessionStorage.getItem('authToken');
    const userEmail = sessionStorage.getItem('userEmail');
    let template;

    if (authToken === null) {
        template = html`
            <nav>
                <a href="/all-memes">All Memes</a>
                <div class="guest">
                    <div class="profile">
                        <a href="/login">Login</a>
                        <a href="/register">Register</a>
                    </div>
                    <a class="active" href="/">Home Page</a>
                </div>
            </nav>`;
    }
    else {
        template = html`
            <nav>
                <a href="/all-memes"">All Memes</a>
                <div class="user">
                    <a href="/create">Create Meme</a>
                    <div class="profile">
                        <span>Welcome, ${userEmail}</span>
                        <a href="/my-profile">My Profile</a>
                        <a @click="${logoutUser}" href="javascript:void(0)">Logout</a>
                    </div>
                </div>
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