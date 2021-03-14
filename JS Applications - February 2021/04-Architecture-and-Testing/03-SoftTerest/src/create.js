import {html, render} from 'https://unpkg.com/lit-html?module';
import {setupCatalog} from "./catalog.js";

const section = document.getElementById('page');

export function createView() {
    const authToken = sessionStorage.getItem('authToken');
    if (authToken === null) {
        return alert('Suspicious operation.');
    }

    const template = html`
    <div class="container home wrapper  my-md-5 pl-md-5">
        <div class=" d-md-flex flex-mb-equal ">
            <div class="col-md-6">
                <img class="responsive-ideas create" src="./images/creativity_painted_face.jpg" alt="">
            </div>
            <form @submit="${createIdea}" class="form-idea col-md-5">
                <div class="text-center mb-4">
                    <h1 class="h3 mb-3 font-weight-normal">Share Your Idea</h1>
                </div>
                <div class="form-label-group">
                    <label for="ideaTitle">Title</label>
                    <input type="text" id="title" name="title" class="form-control" placeholder="What is your idea?"
                           required="" autofocus="">
                </div>
                <div class="form-label-group">
                    <label for="ideaDescription">Description</label>
                    <textarea type="text" name="description" class="form-control" placeholder="Description"
                              required=""></textarea>
                </div>
                <div class="form-label-group">
                    <label for="inputURL">Add Image</label>
                    <input type="text" id="imageURL" name="imageURL" class="form-control" placeholder="Image URL"
                           required="">

                </div>
                <button class="btn btn-lg btn-dark btn-block" type="submit">Create</button>

                <p class="mt-5 mb-3 text-muted text-center">© SoftTerest - 2021.</p>
            </form>
        </div>
    </div>`;
    render(template, section);
}

async function createIdea(e) {
    e.preventDefault();

    const authToken = sessionStorage.getItem('authToken');
    const formData = new FormData(e.target);

    const title = formData.get('title');
    const description = formData.get('description');
    const img = formData.get('imageURL');

    await fetch('http://localhost:3030/data/ideas', {
        method: 'POST',
        headers: {'X-Authorization': authToken},
        body: JSON.stringify({title, description, img})
    });
    await setupCatalog();
}