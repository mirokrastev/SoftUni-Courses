import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import {logoutUser} from "./auth/logout.js";

const main = document.getElementById('navBar');

export function setupNavbar() {
    const authToken = sessionStorage.getItem('authToken');
    let template;

    if (authToken === null) {
        template = html`
            <ul>
                <li class="site-logo">Shoe</li>
                <li>
                    <a href="/">
                        <img src="../public/sneakers.png" alt="">
                    </a>
                </li>
                <li class="site-logo">Shelf</li>
            </ul>`;
    }
    else {
        const userEmail = sessionStorage.getItem('userEmail');
        template = html`
            <ul>
                <li>
                    <a href="/create">Create new offer</a>
                </li>
                <li>
                    <a href="/">
                        <img src="../public/sneakers.png" alt="">
                    </a>
                </li>
                <li>Welcome, ${userEmail} |
                    <a @click="${async () => await logoutUser()}" href="javascript:void(0)">Logout</a>
                </li>
            </ul>`;
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