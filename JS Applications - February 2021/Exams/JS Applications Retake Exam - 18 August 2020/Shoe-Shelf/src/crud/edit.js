import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder(object) {
    return html`
        <h1>Edit Offer</h1>
        <p class="message"></p>
        <form @submit="${async (e) => await changeFunc(e, object._id)}">
            <div>
                <input type="text" value="${object.name}" name="name" placeholder="Name...">
            </div>
            <div>
                <input type="text" value="${object.price}" name="price" placeholder="Price...">
            </div>
            <div>
                <input type="text" value="${object.imageUrl}" name="imageUrl" placeholder="Image url...">
            </div>
            <div>
                <textarea name="description" placeholder="Give us some description about this offer...">
                    ${object.description}
                </textarea>
            </div>
            <div>
                <input type="text" name="brand" value="${object.brand}" placeholder="Brand...">
            </div>
            <div>
                <button>Edit</button>
            </div>
        </form>`;
}

export async function editView(ctx) {
    setupNavbar();
    const id = ctx.params.id;
    const object = await api.get(`data/shoes/` + id);

    const template = templateBuilder(object);
    render(template, main);
}

async function changeFunc(e, id) {
    e.preventDefault();

    const data = FormDataPairs(new FormData(e.target));

    try {
        const result = await api.put(`data/shoes/` + id, data, true);
        page.redirect(`/details/${id}`);
    }
    catch (e) {
        return alert(e.message);
    }
}