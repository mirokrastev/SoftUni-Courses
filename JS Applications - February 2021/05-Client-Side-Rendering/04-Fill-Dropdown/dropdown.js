import {html, render} from 'https://unpkg.com/lit-html?module'

const selectMenu = document.getElementById('menu');

document.querySelector('form')
    .addEventListener('submit', async (e) => {
        e.preventDefault();
        const text = e.target.querySelector('#itemText');
        await fetch('http://localhost:3030/jsonstore/advanced/dropdown', {
            method: 'POST',
            body: JSON.stringify({text: text.value})
        });
        e.target.querySelector('#itemText').value = '';
        return await main();
    })

async function main() {
    const data = [...Object.values(await (await fetch('http://localhost:3030/jsonstore/advanced/dropdown')).json())];
    const template = html`
        ${data.map(e => html`<option value=${e._id}>${e.text}</option>`)}`;

    render(template, selectMenu);
}

main();