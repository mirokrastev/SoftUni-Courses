import {html, render} from 'https://unpkg.com/lit-html?module';

const mainT = document.getElementById('mainT');
const searchBtn = document.getElementById('searchBtn');

searchBtn.addEventListener('click', traverse);

async function main() {
    const data = [...Object.values(await (await fetch('http://localhost:3030/jsonstore/advanced/table')).json())];
    console.log(data);
    let template = html`
        ${data.map(e => html`<tr>
                            <td>${e.firstName} ${e.lastName}</td>
                            <td>${e.email}</td>
                            <td>${e.course}</td>
                         </tr>`)}`;

    render(template, mainT);
}

function traverse() {
    const wordToSearch = document.querySelector('#searchField').value.toLowerCase();
    [...mainT.children].forEach(row => {
        let match = false;
        [...row.children].forEach(col => {
            if (col.textContent.toLowerCase().includes(wordToSearch)) {
                row.className = 'select';
                match = true;
            }
        })
        if (!match) {
            row.removeAttribute('class');
        }
    })
}

main();