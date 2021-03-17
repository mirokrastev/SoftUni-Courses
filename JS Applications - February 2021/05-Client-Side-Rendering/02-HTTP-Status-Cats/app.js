import {html, render} from 'https://unpkg.com/lit-html?module'
import {cats} from './catSeeder.js'

const catSection = document.querySelector('#allCats');

const template = html`
    <ul>
        ${cats.map(cat => html`<li>
            <img src=${cat.imageLocation} width=250 height=250 alt="Card Image Cap">
            <div class=info>
                <button @click=${show} class=showBtn>Show status code</button>
            </div>
            <div class=status style="display: none" id=${cat.id}>
                <h4 class="card-title">Status Code: ${cat.statusCode}</h4>
                <p class="card-text">${cat.statusMessage}</p>
            </div>
        </li>`)}
    </ul>`;

function show(e) {
    const el = e.target.parentElement.parentElement
    const status = el.querySelector('.status');
    const btn = el.querySelector('.showBtn');

    if (status.style.display === 'block') {
        status.style.display = 'none';
        btn.textContent = 'Show status code';
    }
    else {
        status.style.display = 'block';
        btn.textContent = 'Hide status code';
    }
}

render(template, catSection);