import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";
import {deleteFunc} from "./delete.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder(object, buyersArray) {
    return html`
        <div class="offer-details">
            <h1>${object.brand} ${object.name}</h1>
            <div class="info">
                <img src="${object.imageUrl}"
                     alt="">
                <div class="description">${object.description}
                    <br>
                    <br>
                    <p class="price">$${object.price}</p>
                </div>
            </div>
            ${checkAuth(object, buyersArray)}
        </div>`;
}

export async function detailedView(ctx) {
    setupNavbar();
    const id = ctx.params.id;
    try {
        const buyersArray = (await api.get(`data/shoes/${id}`)).people;
        const object = await api.get('data/shoes/' + id);
        const template = templateBuilder(object, buyersArray);
        render(template, main);
    } catch (e) {
        return alert(e.message);
    }
}

function checkAuth(object, buyersArray) {
    const userId = sessionStorage.getItem('userId');
    const userEmail = sessionStorage.getItem('userEmail');

    const allBuyers = buyersArray.length;
    const alreadyBought = Boolean(buyersArray.find(e => e === userEmail));

    if (object._ownerId === userId) {
        return html`
            <div class="actions">
                <span>Buyers: ${allBuyers}</span>
                <a href="/edit/${object._id}">Edit</a>
                <a @click="${async () => await deleteFunc(object._id)}">Delete</a>
            </div>
        `;
    }

    if (alreadyBought) {
        return html`
        <div class="actions">
            <span>Buyers: ${allBuyers}</span>
            <span>You bought it</span>
        </div>
        `
    }
    return html`
        <div class="actions">
            <span>Buyers: ${allBuyers}</span>
            <a @click="${async () => await buyObject(object)}">Buy</a>
        </div>`;
}

async function buyObject(object) {
    const userEmail = sessionStorage.getItem('userEmail');
    console.log(object)
    object.people.push(userEmail);


    await api.put('data/shoes/' + object._id, object, true);
    page.redirect('/details/' + object._id);
}