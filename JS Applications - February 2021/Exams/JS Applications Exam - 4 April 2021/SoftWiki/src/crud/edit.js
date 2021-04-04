import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder(object) {
    return html`
        <section id="edit-page" class="content">
            <h1>Edit Article</h1>

            <form id="edit" @submit="${async (e) => await changeFunc(e, object._id)}">
                <fieldset>
                    <p class="field title">
                        <label for="title">Title:</label>
                        <input type="text" value="${object.title}" name="title" id="title" placeholder="Enter article title">
                    </p>

                    <p class="field category">
                        <label for="category">Category:</label>
                        <input type="text" value="${object.category}" name="category" id="category" placeholder="Enter article category">
                    </p>
                    <p class="field">
                        <label for="content">Content:</label>
                        <textarea name="content" id="content">${object.content}</textarea>
                    </p>

                    <p class="field submit">
                        <input class="btn submit" type="submit" value="Save Changes">
                    </p>

                </fieldset>
            </form>
        </section>`;
}

export async function editView(ctx) {
    setupNavbar();

    const id = ctx.params.id;
    const object = await api.get(`data/wiki/` + id);

    const template = templateBuilder(object);
    render(template, main);
}

async function changeFunc(e, id) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const data = FormDataPairs(formData);

    if (!data['title'] || !data['content'] || !data['category'])
        return alert('Invalid form.');

    if (!['JavaScript', 'C#', 'Java', 'Python'].find(e => e === data['category']))
        return alert('Invalid category!');

    try {
        const result = await api.put(`data/wiki/` + id, data, true);
        page.redirect(`/details/${id}`);
    }
    catch (e) {
        return alert(e.message);
    }
}