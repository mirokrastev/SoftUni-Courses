function solve() {
    let formElement = document.getElementsByTagName('form')[0];
    formElement.addEventListener('submit', (event) => event.preventDefault());

    let taskAddButton = document.querySelector('#add');
    taskAddButton.addEventListener('click', checkInput);

    let openTab = document.querySelector('.wrapper > section:nth-child(2) > div:nth-child(2)');

    let inProgressDiv = document.getElementById('in-progress');

    let completeDiv = document.querySelector('.wrapper > section:nth-child(4) > div:nth-child(2)');

    function deleteTask(event) {
        event.target.parentElement.parentElement.remove();
    }

    function checkInput() {
        let [task, desc, dueDate] = [document.getElementById('task'),
                                    document.getElementById('description'),
                                    document.getElementById('date')];

        if (!task.value || !desc.value || !dueDate.value) return;
        addToOpen(task.value, desc.value, dueDate.value);
    }

    function addToOpen(task, desc, dueDate) {
        let newArticle = document.createElement('article');
        newArticle.innerHTML += `<h3>${task}</h3>
                                 <p>Description: ${desc}</p>
                                 <p>Due Date: ${dueDate}</p>`;
        let newDiv = document.createElement('div');
        newDiv.setAttribute('class', 'flex');

        let startButton = document.createElement('button');
        startButton.innerText = 'Start';
        startButton.setAttribute('class', 'green');
        startButton.addEventListener('click', moveToProgress)

        let deleteButton = document.createElement('button');
        deleteButton.innerText = 'Delete';
        deleteButton.setAttribute('class', 'red');
        deleteButton.addEventListener('click', deleteTask);

        newDiv.appendChild(startButton);
        newDiv.appendChild(deleteButton);
        newArticle.appendChild(newDiv);

        openTab.appendChild(newArticle);
    }

    function moveToProgress(event) {
        let obj = event.target.parentElement.parentElement;
        obj.removeChild(obj.getElementsByTagName('div')[0]);

        let newDiv = document.createElement('div');
        newDiv.setAttribute('class', 'flex');

        let finishButton = document.createElement('button');
        finishButton.innerText = 'Finish';
        finishButton.setAttribute('class', 'orange');

        let deleteButton = document.createElement('button');
        deleteButton.innerText = 'Delete';
        deleteButton.setAttribute('class', 'red');
        deleteButton.addEventListener('click', deleteTask);

        newDiv.appendChild(deleteButton);
        newDiv.appendChild(finishButton);

        finishButton.addEventListener('click', moveToComplete);
        obj.appendChild(newDiv);

        openTab.removeChild(obj);

        inProgressDiv.appendChild(obj);
    }

    function moveToComplete(event) {
        let obj = event.target.parentElement.parentElement;

        obj.removeChild(obj.getElementsByTagName('div')[0]);
        inProgressDiv.removeChild(obj);
        completeDiv.appendChild(obj);
    }
}