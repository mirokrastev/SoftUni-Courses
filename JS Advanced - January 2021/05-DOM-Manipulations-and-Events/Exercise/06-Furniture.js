function solve() {
    let generateButton = document.getElementsByTagName('button')[0];
    let jsonObjsTextArea = document.getElementsByTagName('textarea')[0];
    let mainTBody = document.getElementsByTagName('tbody')[0];
    let buyButton = document.getElementsByTagName('button')[1];

    let finalProductsTextArea = document.getElementsByTagName('textarea')[1];


    generateButton.addEventListener('click', generateObjects);
    buyButton.addEventListener('click', buyObjects);

    function generateObjects() {
        let objs = JSON.parse(jsonObjsTextArea.value);

        for (let obj of objs ) {
            let newTr = document.createElement('tr');

            let tdImage = document.createElement('td');
            let imageObj = document.createElement('img');
            imageObj.src = obj['img']
            tdImage.appendChild(imageObj);

            let tdName = document.createElement('td');
            let pTagName = document.createElement('p');
            pTagName.innerText = obj['name'];
            tdName.appendChild(pTagName);

            let tdPrice = document.createElement('td');
            let pTagPrice = document.createElement('p');
            pTagPrice.innerText = obj['price'];
            tdPrice.appendChild(pTagPrice);

            let tdDecFactor = document.createElement('td');
            let pTagDecFactor = document.createElement('p');
            pTagDecFactor.innerText = obj['decFactor'];
            tdDecFactor.appendChild(pTagDecFactor);

            let tdInputCheckbox = document.createElement('td');
            let inputCheckBox = document.createElement('input');
            inputCheckBox.type = 'checkbox';
            tdInputCheckbox.appendChild(inputCheckBox);

            newTr.appendChild(tdImage);
            newTr.appendChild(tdName);
            newTr.appendChild(tdPrice);
            newTr.appendChild(tdDecFactor);
            newTr.appendChild(tdInputCheckbox);

            mainTBody.appendChild(newTr);
        }
    }

    function buyObjects() {
        let boughtObjectsArray = [];
        let totalPrice = 0;
        let decFactor = 0;
        for (let obj of Array.from(mainTBody.children)) {
            if (obj.cells[4].children[0].checked) {
                boughtObjectsArray.push(obj.cells[1].children[0].innerText);
                totalPrice += Number(obj.cells[2].children[0].innerText);
                decFactor += Number(obj.cells[3].children[0].innerText);
            }
        }
        finalProductsTextArea.innerHTML = `Bought furniture: ${boughtObjectsArray.join(', ')}\n`;
        finalProductsTextArea.innerHTML += `Total price: ${totalPrice.toFixed(2)}\n`;
        finalProductsTextArea.innerHTML += `Average decoration factor: ${decFactor / boughtObjectsArray.length}`;
    }
}