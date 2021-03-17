import {html, render} from 'https://unpkg.com/lit-html?module';
import {towns} from './towns.js'

const townsDiv = document.querySelector('#towns');
const searchBtn = document.querySelector('button');
const inputField = document.getElementById('searchText');
const resultField = document.getElementById('result');

searchBtn.addEventListener('click', search);

function search() {
    const searchValue = inputField.value.toLowerCase();
    let matches = 0;
    let template = html`
    <ul>
        ${towns.map(e => {
            if (e.toLowerCase().includes(searchValue) && searchValue !== '') {
                matches++;
                return html`
                    <li class="active">${e}</li>`;
            }
            return html`<li>${e}</li>`;
        })}
    </ul>`;

    if (matches > 0) {
        resultField.textContent = `${matches} matches found`;
    }
    else {
        resultField.textContent = '';
    }

    render(template, townsDiv);
}

function onLoad() {
    let template = html`
    <ul>
        ${towns.map(e => html`<li>${e}</li>`)}
    </ul>`;

    render(template, townsDiv);
}

onLoad();