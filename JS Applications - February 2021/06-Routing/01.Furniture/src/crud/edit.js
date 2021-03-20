import {html, render} from 'https://unpkg.com/lit-html?module';
import {setupNavbar} from "../navbar.js";
import {checkAuth} from "../auth/checkAuth.js";
import {processForm} from "./processForm.js";

const main = document.getElementById('main');
const additional = document.getElementById('additional');

function templateBuilder(object, objId) {
    return html`
        <form @submit="${е => processForm(е, 'put', objId)}">
            <div class="row space-top">
                <div class="col-md-4">
                    <div class="form-group">
                        <label class="form-control-label" for="new-make">Make</label>
                        <input class="form-control" id="new-make" type="text" name="make" value="${object.make}">
                    </div>
                    <div class="form-group has-success">
                        <label class="form-control-label" for="new-model">Model</label>
                        <input class="form-control" id="new-model" type="text" name="model" value="${object.model}">
                    </div>
                    <div class="form-group has-danger">
                        <label class="form-control-label" for="new-year">Year</label>
                        <input class="form-control" id="new-year" type="number" name="year" value="${object.year}">
                    </div>
                    <div class="form-group">
                        <label class="form-control-label" for="new-description">Description</label>
                        <input class="form-control" id="new-description" type="text" name="description" value="${object.description}">
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="form-group">
                        <label class="form-control-label" for="new-price">Price</label>
                        <input class="form-control" id="new-price" type="number" name="price" value="${object.price}">
                    </div>
                    <div class="form-group">
                        <label class="form-control-label" for="new-image">Image</label>
                        <input class="form-control" id="new-image" type="text" name="img" value="${object.img}">
                    </div>
                    <div class="form-group">
                        <label class="form-control-label" for="new-material">Material (optional)</label>
                        <input class="form-control" id="new-material" type="text" name="material" value="${object.material}">
                    </div>
                    <input type="submit" class="btn btn-info" value="Edit" />
                </div>
            </div>
        </form>`;
}

export async function editView(ctx) {
    setupNavbar('none');
    checkAuth();

    const objId = ctx.params.id;
    const object = await (await fetch(`http://localhost:3030/data/catalog/${objId}`)).json();

    const additionalTemplate = html`<h1>Edit Furniture</h1><p>Please fill all fields.</p>`;
    render(additionalTemplate, additional);

    const template = templateBuilder(object, objId);
    render(template, main);
}