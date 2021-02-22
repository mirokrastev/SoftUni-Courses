function solution() {
    let addGiftButton = document.querySelector('section.card:nth-child(1) > div:nth-child(2) > button:nth-child(2)');
    addGiftButton.addEventListener('click', validateInput);

    function validateInput() {
        let giftNameField = document.querySelector('section.card:nth-child(1) > div:nth-child(2) > input:nth-child(1)');
        let listOfGiftsUl = document.querySelector('section.card:nth-child(2) > ul:nth-child(2)');

        let newLi = document.createElement('li');
        newLi.className = 'gift';
        newLi.textContent += giftNameField.value;

        let sendButton = document.createElement('button');
        sendButton.textContent = 'Send';
        sendButton.id = 'sendButton';
        sendButton.addEventListener('click', (e) => {
            let newSentGiftLi = document.createElement('li');
            newSentGiftLi.className = 'gift';
            newSentGiftLi.textContent = e.target.parentElement.textContent.slice(0,
                e.target.parentElement.textContent.indexOf('SendDiscard'));
            let sentGiftUlSection = document.querySelector('section.card:nth-child(3) > ul:nth-child(2)');
            sentGiftUlSection.appendChild(newSentGiftLi);
            e.target.parentElement.remove();
        })
        newLi.appendChild(sendButton);

        let discardButton = document.createElement('button');
        discardButton.textContent = 'Discard';
        discardButton.id = 'discardButton';
        discardButton.addEventListener('click', (e) => {
            let newDiscardedLi = document.createElement('li');
            newDiscardedLi.className = 'gift';
            newDiscardedLi.textContent = e.target.parentElement.textContent.slice(0,
                e.target.parentElement.textContent.indexOf('SendDiscard'));
            let discardedUlSection = document.querySelector('section.card:nth-child(4) > ul:nth-child(2)');
            discardedUlSection.appendChild(newDiscardedLi);
            e.target.parentElement.remove();
        })
        newLi.appendChild(discardButton);

        listOfGiftsUl.appendChild(newLi);

        sortObjects();

        giftNameField.value = '';
    }

    function sortObjects() {
        let listOfGiftsUl = document.querySelector('section.card:nth-child(2) > ul:nth-child(2)');
        Array.from(listOfGiftsUl.children)
            .sort((a, b) =>
                a.textContent.slice(0, a.textContent.indexOf('SendDiscard'))
                    .localeCompare(b.textContent.slice(0, b.textContent.indexOf('sendDiscard'))))
            .forEach(node => listOfGiftsUl.appendChild(node));
    }
}