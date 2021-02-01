function lockedProfile() {
    let mainEl = document.getElementById('main');

    for (let divEl of Array.from(mainEl.children)) {
        let btn = divEl.getElementsByTagName('button')[0];
        btn.addEventListener('click', btnAction);

        let name = divEl.children[2].name;
        let radioButtons = document.getElementsByName(name);

        for (let radioButton of Array.from(radioButtons)) {
            radioButton.addEventListener('change', checkConditions);
        }
    }

    function btnAction(event) {
        let name = event.target.parentElement.children[2].name;
        let radioButtons = document.getElementsByName(name);

        if (!radioButtons[1].checked) {
            return;
        }
        else {
            showMore(event, radioButtons, name);
        }
    }

    function showMore(event, radioButton, name) {
        let button = event.target;
        let divEl = document.getElementById('user'+name.split('user')[1][0]+'HiddenFields');

        if (button.innerText === 'Show more') {
            button.innerText = 'Hide it';
            divEl.style.display = 'block';
        }
        else if (button.innerText === 'Hide it') {
            divEl.style.display = 'none';
            button.innerText = 'Show more';
        }
    }

    function hideDiv(element) {
        let btn = element.getElementsByTagName('button')[0];
        let divElToHide = element.getElementsByTagName('div')[0];
        btn.innerText = 'Show more';
        divElToHide.style.display = 'none';
    }

    function checkConditions(event) {
        let btn = event.target.parentElement.getElementsByTagName('button')[0];
        if (event.target.checked && btn.innerText === 'Hide it') {
            hideDiv(event.target.parentElement)
        }
    }
}