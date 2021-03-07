const mainSection = document.getElementById('main');

function solution() {
    fetch('http://localhost:3030/jsonstore/advanced/articles/list')
        .then(response => response.json())
        .then(data => {
            data.forEach(e => createAccordion(e));
        })
}

function createAccordion(object) {
    mainSection.innerHTML += `
    <div class="accordion">
        <div class="head">
            <span>${object.title}</span>
            <button class="button" id="${object._id}" onclick="getMoreInfo(this.parentElement.parentElement)">More</button>
        </div>
    </div>`;
}

async function getMoreInfo(accordion) {
    let accordionButton = accordion.querySelector('button');
    const accordionId = accordionButton.id;

    if (accordionButton.textContent === 'Less') {
        accordionButton.textContent = 'More';
        accordion.querySelector('.extra').remove();
        return;
    }

    let response = await fetch(`http://localhost:3030/jsonstore/advanced/articles/details/${accordionId}`);
    let json = await response.json();

    accordionButton.textContent = 'Less';
    accordion.innerHTML += `
    <div class="extra">
        <p>${json.content}</p>
    </div>`;
    accordion.querySelector('div > .extra').style.display = 'inline-block';
}

solution();