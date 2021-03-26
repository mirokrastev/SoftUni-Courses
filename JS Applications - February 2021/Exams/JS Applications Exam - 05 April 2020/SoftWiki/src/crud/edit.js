import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder(object) {
    return html`
        <div class="container">

            <form @submit="${async (e) => await changeFunc(e, object._id)}">
                <fieldset>
                    <legend>Edit article</legend>
                    <p class="field title">
                        <input type="text" value="${object.title}" name="title" id="title" placeholder="Arrays">
                        <label for="title">Title:</label>
                    </p>

                    <p class="field category">
                        <input type="text" value="${object.category}" name="category" id="category" placeholder="JavaScript">
                        <label for="category">Category:</label>
                    </p>
                    <p class="field content">
                        <textarea name="content" id="content">${object.content}</textarea>
                        <label for="content">Content:</label>
                    </p>

                    <p class="field submit">
                        <button class="btn submit" type="submit">Edit</button>
                    </p>

                </fieldset>
            </form>
        </div>`;
}

export async function editView(ctx) {
    setupNavbar();

    const id = ctx.params.id;
    const object = await api.get(`data/articles/` + id, true);

    const template = templateBuilder(object);
    render(template, main);
}

async function changeFunc(e, id) {
    e.preventDefault();

    const data = FormDataPairs(new FormData(e.target));

    try {
        const result = await api.put(`data/articles/` + id, data, true);
        page.redirect(`/`);
    }
    catch (e) {
        return alert(e.message);
    }
}