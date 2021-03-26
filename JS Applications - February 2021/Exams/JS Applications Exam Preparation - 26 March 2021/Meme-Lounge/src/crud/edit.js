import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";
import {clearNotification, makeNotification} from "../notification.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder(object) {
    // @submit="${async (e) => await changeFunc(e, object._id)}" ON FORM
    return html`
        <section id="edit-meme">
            <form @submit="${async (e) => await changeFunc(e, object._id)}" id="edit-form">
                <h1>Edit Meme</h1>
                <div class="container">
                    <label for="title">Title</label>
                    <input value="${object.title}" id="title" type="text" placeholder="Enter Title" name="title">
                    <label for="description">Description</label>
                    <textarea id="description" placeholder="Enter Description" name="description">
                            ${object.description}
                        </textarea>
                    <label for="imageUrl">Image Url</label>
                    <input value="${object.imageUrl}" id="imageUrl" type="text" placeholder="Enter Meme ImageUrl" name="imageUrl">
                    <input type="submit" class="registerbtn button" value="Edit Meme">
                </div>
            </form>
        </section>`;
}



export async function editView(ctx) {
    setupNavbar();
    clearNotification();

    const id = ctx.params.id;
    const object = await api.get(`data/memes/` + id);

    const template = templateBuilder(object);
    render(template, main);
}

async function changeFunc(e, id) {
    e.preventDefault();

    const data = FormDataPairs(new FormData(e.target));

    if (!data['title'] || !data['description'] || !data['imageUrl']) {
        return makeNotification('Invalid form.');
    }

    try {
        const result = await api.put(`data/memes/` + id, data, true);
        page.redirect(`/details/${id}`);
    }
    catch (e) {
        makeNotification(e.message);
    }
}