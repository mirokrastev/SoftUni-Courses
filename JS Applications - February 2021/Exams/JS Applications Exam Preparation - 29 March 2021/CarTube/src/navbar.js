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
                <nav>
                    <a class="active" href="/">Home</a>
                    <a href="/all-listings">All Listings</a>
                    <a href="/search">By Year</a>
                    <div id="guest">
                        <a href="/login">Login</a>
                        <a href="/register">Register</a>
                    </div>
                </nav>
            </header>`;
    }
    else {
        const username = sessionStorage.getItem('userName');
        template = html`
            <header>
                <nav>
                    <a class="active" href="/">Home</a>
                    <a href="/all-listings">All Listings</a>
                    <a href="/search">By Year</a>
                    <div id="profile">
                        <a>Welcome ${username}</a>
                        <a href="/my-listings">My Listings</a>
                        <a href="/create">Create Listing</a>
                        <a @click="${logoutUser}" href="javascript:void(0)">Logout</a>
                    </div>
                </nav>
            </header>`;
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