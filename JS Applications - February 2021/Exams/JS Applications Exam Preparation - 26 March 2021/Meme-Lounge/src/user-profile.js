import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import apiReq from "./api/request.js";
import {setupNavbar} from "./navbar.js";
import {clearNotification} from "./notification.js";

const main = document.getElementById('mainContent');
const api = apiReq();
const mapper = {
    'male': '/images/male.png',
    'female': '/images/female.png'
}

function templateBuilder(object, username, email, gender) {
    return html`
        <section id="user-profile-page" class="user-profile">
            <article class="user-info">
                <img id="user-avatar-url" alt="user-profile" src="${mapper[gender]}">
                <div class="user-content">
                    <p>Username: ${username}</p>
                    <p>Email: ${email}</p>
                    <p>My memes count: ${object.length}</p>
                </div>
            </article>
            <h1 id="user-listings-title">User Memes</h1>
            ${checkCondition(object)}
        </section>`
}

export async function userProfileView() {
    setupNavbar();
    clearNotification();

    const userId = sessionStorage.getItem('userId');
    const userGender = sessionStorage.getItem('gender');
    const userName = sessionStorage.getItem('userName');
    const email = sessionStorage.getItem('userEmail');
    const userMemes = await api.get(`data/memes?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`);

    const template = templateBuilder(userMemes, userName, email, userGender);

    render(template, main);
}

function checkCondition(object) {
    if (object.length === 0) {
        return html`<p class="no-memes">No memes in database.</p>`;
    }
    return html`
        <div class="user-meme-listings">
            ${object.map(e => html`
                <div class="user-meme">
                    <p class="user-meme-title">${e.title}</p>
                    <img class="userProfileImage" alt="meme-img" src="${e.imageUrl}">
                    <a class="button" href="/details/${e._id}">Details</a>
                </div>`)}
        </div>`;
}

// <section id="user-profile-page" className="user-profile">
//     <article className="user-info">
//         <img id="user-avatar-url" alt="user-profile" src="/images/female.png">
//             <div className="user-content">
//                 <p>Username: Mary</p>
//                 <p>Email: mary@abv.bg</p>
//                 <p>My memes count: 2</p>
//             </div>
//     </article>
//     <h1 id="user-listings-title">User Memes</h1>
//     <div className="user-meme-listings">
//         <!-- Display : All created memes by this user (If any) -->
//         <div className="user-meme">
//             <p className="user-meme-title">Java Script joke</p>
//             <img className="userProfileImage" alt="meme-img" src="/images/1.png">
//                 <a className="button" href="#">Details</a>
//         </div>
//         <div className="user-meme">
//             <p className="user-meme-title">Bad code can present some problems</p>
//             <img className="userProfileImage" alt="meme-img" src="/images/3.png">
//                 <a className="button" href="#">Details</a>
//         </div>
//
//         <!-- Display : If user doesn't have own memes  -->
//         <p className="no-memes">No memes in database.</p>
//     </div>
// </section>