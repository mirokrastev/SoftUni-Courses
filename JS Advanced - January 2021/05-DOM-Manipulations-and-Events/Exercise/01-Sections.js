function create(words) {
    let contentDiv = document.getElementById('content');

    words.forEach(word => {
        let section = document.createElement('div');
        let pTag = document.createElement('p');
        pTag.textContent = word;
        pTag.style.display = 'none';
        section.appendChild(pTag);

        section.addEventListener('click', (event) => {
            event.currentTarget.querySelector('p').style.display = 'block';
        })
        contentDiv.appendChild(section);
    })
}