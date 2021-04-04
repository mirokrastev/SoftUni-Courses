import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder(object) {
    // @submit="${async (e) => await changeFunc(e, object._id)}" ON FORM
    return html`
        <section id="edit-listing">
            <div class="container">

                <form @submit="${async (e) => await changeFunc(e, object._id)}" id="edit-form">
                    <h1>Edit Car Listing</h1>
                    <p>Please fill in this form to edit an listing.</p>
                    <hr>

                    <p>Car Brand</p>
                    <input type="text" placeholder="Enter Car Brand" name="brand" value="${object.brand}">

                    <p>Car Model</p>
                    <input type="text" placeholder="Enter Car Model" name="model" value="${object.model}">

                    <p>Description</p>
                    <input type="text" placeholder="Enter Description" name="description" value="${object.description}">

                    <p>Car Year</p>
                    <input type="number" placeholder="Enter Car Year" name="year" value="${object.year}">

                    <p>Car Image</p>
                    <input type="text" placeholder="Enter Car Image" name="imageUrl" value="${object.imageUrl}">

                    <p>Car Price</p>
                    <input type="number" placeholder="Enter Car Price" name="price" value="${object.price}">

                    <hr>
                    <input type="submit" class="registerbtn" value="Edit Listing">
                </form>
            </div>
        </section>`;
}

export async function editView(ctx) {
    setupNavbar();

    const id = ctx.params.id;
    const object = await api.get(`data/cars/` + id);

    const template = templateBuilder(object);
    render(template, main);
}

async function changeFunc(e, id) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const data = FormDataPairs(formData);

    data['year'] = Number(data['year']);
    data['price'] = Number(data['price'])

    if (Number(data['year']) <= 0 || Number(data['price']) <= 0) {
        return alert('Year and Price must be positive numbers.');
    }

    try {
        const result = await api.put(`data/cars/` + id, data, true);
        page.redirect(`/details/${id}`);
    }
    catch (e) {
        return alert(e.message);
    }
}