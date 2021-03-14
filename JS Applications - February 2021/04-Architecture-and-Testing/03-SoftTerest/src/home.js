import {html, render} from 'https://unpkg.com/lit-html?module';
import {setupCatalog} from "./catalog.js";

const section = document.getElementById('page');

export function setupHome() {
    const template = html`
        <div class="container home wrapper  my-md-5 pl-md-5">
        <div class="d-md-flex flex-md-equal">
            <div class="col-md-5">
                <img class="responsive" src="./images/01.svg"/>
            </div>
            <div class="home-text col-md-7">
                <h2 class="featurette-heading">Do you wonder if your idea is good?</h2>
                <p class="lead">Join our family =)</p>
                <p class="lead">Post your ideas!</p>
                <p class="lead">Find what other people think!</p>
                <p class="lead">Comment on other people's ideas.</p>
            </div>
        </div>
        <div class="bottom text-center">
            <a @click="${setupCatalog}" class="btn btn-secondary btn-lg">Get Started</a>
        </div>
        </div>`;
    render(template, section);
}