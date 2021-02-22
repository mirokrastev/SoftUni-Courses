function solve() {
    let addButton = document.querySelector("body > main > section.admin-view.section-view > div > div > form > div:nth-child(4) > button");
    addButton.addEventListener('click', validateInput);

    function validateInput(e) {
        e.preventDefault();

        let lectureNameField = document.querySelector("body > main > section.admin-view.section-view > div > div > form > div:nth-child(1) > input[type=text]");
        let dateField = document.querySelector("body > main > section.admin-view.section-view > div > div > form > div:nth-child(2) > input[type=datetime-local]");
        let moduleField = document.querySelector("body > main > section.admin-view.section-view > div > div > form > div:nth-child(3) > select");

        if (!lectureNameField.value || !dateField.value || moduleField.value === 'Select module') {
            lectureNameField.value = '';
            dateField.value = '';
            moduleField.value = 'Select module';
            return;
        }

        addToTrainings(lectureNameField, dateField, moduleField);
    }

    function addToTrainings(lectureField, dateField, moduleField) {
        let modulesDiv= document.querySelector("body > main > section.user-view.section-view > div");

        let module = `${moduleField.value.toUpperCase()}-MODULE`;
        let currentModule = Array.from(modulesDiv.getElementsByClassName('module'))

        if (currentModule.length > 0) {
            currentModule = Array.from(currentModule)
                .find(e => e.firstElementChild.textContent === module);
        }
        else {
            currentModule = undefined;
        }
        if (currentModule) {
            let currentModuleLi = currentModule.querySelector('ul');
            createEntry(currentModuleLi, lectureField.value, dateField.value);
            sortObjects(currentModuleLi);
        }
        else {
            let currentModule = document.createElement('div');
            currentModule.className = 'module';
            currentModule.innerHTML += `<h3>${module}</h3><ul></ul>`;

            let currentModuleLi = currentModule.querySelector('ul');
            createEntry(currentModuleLi, lectureField.value, dateField.value);

            modulesDiv.appendChild(currentModule);
            sortObjects(currentModuleLi);
        }

        lectureField.value = '';
        dateField.value = '';
        moduleField.value = 'Select module';
    }

    function createEntry(ul, lectureName, dateField) {
        let [year, month, rest] = dateField.split('-');
        let [day, hour, min] = rest.split(/T|:/);

        let newLi = document.createElement('li');
        newLi.className = 'flex';
        newLi.innerHTML += `<h4>${lectureName} - ${year}/${month}/${day} - ${hour}:${min}</h4>`;


        let delButton = document.createElement('button');
        delButton.className = 'red';
        delButton.textContent = 'Del';
        delButton.addEventListener('click', delEntry);
        newLi.appendChild(delButton);

        ul.appendChild(newLi);
    }

    function delEntry(e) {
         if (Array.from(e.target.parentElement.parentElement.children).length === 1)
             e.target.parentElement.parentElement.parentElement.remove();
         else {
             e.target.parentElement.remove();
         }
    }

    function sortObjects(ul) {
        Array.from(ul.children)
            .sort((a, b) => {
                let firstElH4 = a.querySelector('h4');
                let secondElH4 = b.querySelector('h4');

                let firstDate = firstElH4.textContent.split(' - ').slice(-2).join(' - ');
                let secondDate = secondElH4.textContent.split(' - ').slice(-2).join(' - ');

                return firstDate.localeCompare(secondDate);
            })
            .forEach(node => ul.appendChild(node));
    }
}