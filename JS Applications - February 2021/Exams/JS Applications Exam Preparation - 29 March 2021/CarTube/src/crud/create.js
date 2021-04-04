import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";
import {FormDataPairs} from "../api/data.js";
import {setupNavbar} from "../navbar.js";

const main = document.getElementById('mainContent');
const api = apiReq();

function templateBuilder() {
    return html`
        <section id="create-listing">
            <div class="container">
                <form @submit="${createFunc}" id="create-form">
                    <h1>Create Car Listing</h1>
                    <p>Please fill in this form to create an listing.</p>
                    <hr>

                    <p>Car Brand</p>
                    <input type="text" placeholder="Enter Car Brand" name="brand">

                    <p>Car Model</p>
                    <input type="text" placeholder="Enter Car Model" name="model">

                    <p>Description</p>
                    <input type="text" placeholder="Enter Description" name="description">

                    <p>Car Year</p>
                    <input type="number" placeholder="Enter Car Year" name="year">

                    <p>Car Image</p>
                    <input type="text" placeholder="Enter Car Image" name="imageUrl">

                    <p>Car Price</p>
                    <input type="number" placeholder="Enter Car Price" name="price">

                    <hr>
                    <input type="submit" class="registerbtn" value="Create Listing">
                </form>
            </div>
        </section>`;
}

export function createView() {
    setupNavbar();
    
    const template = templateBuilder();
    render(template, main);
}

async function createFunc(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const data = FormDataPairs(formData);

    data['year'] = Number(data['year']);
    data['price'] = Number(data['price']);

    if (Number(data['year']) <= 0 || Number(data['price']) <= 0) {
        return alert('Year and Price must be positive numbers.');
    }

    try {
        const result = await api.post('data/cars', data, true);
        page.redirect('/all-listings');
    }
    catch (e) {
        return alert(e.message);
    }
}