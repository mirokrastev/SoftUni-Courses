function solve() {
    let onScreenButton = document.querySelector('#container > button');
    onScreenButton.addEventListener('click', processInput);

    let deleteArchiveButton = document.querySelector('#archive > button:nth-child(3)');
    deleteArchiveButton.addEventListener('click', () => {
        Array.from(deleteArchiveButton.parentElement.querySelector('ul').children)
            .forEach(el => el.remove());
    })

    function processInput(event) {
        let moviesSection = document.querySelector('#movies > ul:nth-child(2)');

        event.preventDefault();
        let movieName = document.querySelector('#container > input:nth-child(1)');
        let movieHall = document.querySelector('#container > input:nth-child(2)');
        let movieTicketPrice = document.querySelector('#container > input:nth-child(3)');
        let movieTicketPriceInteger = Number.parseInt(movieTicketPrice.value);
        if (movieName.value === '' || movieHall.value === '' || movieTicketPrice.value === '' || isNaN(movieTicketPriceInteger)) {
            return;
        }

        // Append new li with movie to moviesSection

        let newLi = document.createElement('li');
        newLi.innerHTML += `<span>${movieName.value}</span>
                            <strong>Hall: ${movieHall.value}</strong>`;

        let divElForNewLi = document.createElement('div');
        divElForNewLi.innerHTML += `<strong>${movieTicketPriceInteger.toFixed(2)}</strong>
                                    <input placeholder="Tickets Sold">`;

        let buttonForDiv = document.createElement('button');
        buttonForDiv.textContent = 'Archive';
        buttonForDiv.addEventListener('click', archiveMovie);

        divElForNewLi.appendChild(buttonForDiv);
        newLi.appendChild(divElForNewLi);

        moviesSection.appendChild(newLi);

        movieName.value = '';
        movieHall.value = '';
        movieTicketPrice.value = '';
    }

    function archiveMovie(event) {
        let archivedSection = document.querySelector('#archive > ul:nth-child(2)');

        let toArchive = event.target.parentElement.parentElement;
        let ticketsSoldInteger = Number(toArchive.querySelector('input').value);
        if (!ticketsSoldInteger) {
            return;
        }
        let movieName = toArchive.querySelector('span').textContent;
        let movieTicketPrice = Number(toArchive.querySelector('div strong').textContent);

        let archivedLi = document.createElement('li');

        let totalSoldTickets = ticketsSoldInteger * movieTicketPrice;

        archivedLi.innerHTML += `<span>${movieName}</span>
                                 <strong>Total amount: ${totalSoldTickets.toFixed(2)}</strong>`

        let buttonForLi = document.createElement('button');
        buttonForLi.textContent = 'Delete';
        buttonForLi.addEventListener('click', () => archivedLi.remove());

        archivedLi.appendChild(buttonForLi);

        archivedSection.appendChild(archivedLi);

        toArchive.remove();
    }
}