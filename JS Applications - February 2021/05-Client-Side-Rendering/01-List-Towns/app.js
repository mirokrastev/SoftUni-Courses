import {html, render} from 'https://unpkg.com/lit-html?module'

const rootDiv = document.querySelector('#root');

document.querySelector('form')
.addEventListener('submit', main);


function main(e) {
    e.preventDefault();

    let input = e.target.querySelector('#towns').value.split(', ');

    const htmlResult = html`<ul>${input.map(el => html`<li>${el}</li>`)}</ul>`;
    render(htmlResult, rootDiv);
}