import {html, render} from 'https://unpkg.com/lit-html?module'
import {processForm} from "./api.js";

const loadBtn = document.getElementById('loadBooks');
loadBtn.addEventListener('click', await main);

const tBody = document.querySelector('tbody');
const formDiv = document.getElementById('formDiv');

async function main() {
    let data = await (await fetch('http://localhost:3030/jsonstore/collections/books')).json();
    Object.keys(data)
        .forEach(key => data[key].id = key);
    data = Object.values(data);

    const addForm = html`
        <form @submit="${addEl}" id="add-form">
            <h3>Add book</h3>
            <label>TITLE</label>
            <input type="text" name="title" placeholder="Title...">
            <label>AUTHOR</label>
            <input type="text" name="author" placeholder="Author...">
            <input type="submit" value="Submit">
        </form>`;

    render(template(data), tBody);

    render(addForm, formDiv);
}

const template = (data) => html`
    ${data.map(e => html`<tr>
                            <td>${e.title}</td>
                            <td>${e.author}</td>
                            <td>
                                <button @click="${() => editEl(e)}">Edit</button>
                                <button @click="${() => deleteEl(e.id)}">Delete</button>
                            </td>
                         </tr>`)}`;

async function addEl(e) {
    const [author, title] = processForm(e);

    await fetch(`http://localhost:3030/jsonstore/collections/books`, {
        method: 'POST',
        body: JSON.stringify({author, title})
    });
    return await main();
}

async function editEl(obj) {
    const editForm = html`
        <form @submit="${async (e) => {
            const [author, title] = processForm(e);
            
            await fetch(`http://localhost:3030/jsonstore/collections/books/${obj.id}`, {
            method: 'PUT',
            body: JSON.stringify({author, title})
        });
        return await main();
        }}" id="edit-form">
            <input type="hidden" name="id">
            <h3>Edit book</h3>
            <label>TITLE</label>
            <input type="text" name="title" value=${obj.title} placeholder="Title...">
            <label>AUTHOR</label>
            <input type="text" name="author" value=${obj.author} placeholder="Author...">
            <input type="submit" value="Save">
        </form>`
    render(editForm, formDiv);
}

async function deleteEl(id) {
    await fetch(`http://localhost:3030/jsonstore/collections/books/${id}`, {
        method: 'DELETE'
    });
    return await main();
}