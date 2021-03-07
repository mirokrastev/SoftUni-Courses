const loadBooksButton = document.getElementById('loadBooks');
const bookTitleField = document.getElementById('title');
const bookAuthorField = document.getElementById('author');

const booksTBody = document.getElementById('booksTBody');
const bookForm = document.getElementById('bookForm');

loadBooksButton.addEventListener('click', getBooks);
bookForm.addEventListener('submit', addBook);

let currentId = null;

async function getBooks() {
    let response = await fetch(`http://localhost:3030/jsonstore/collections/books`);
    let json = await response.json();
    booksTBody.innerHTML = '';

    Object.keys(json)
        .forEach(key => {
            let newBookTr = document.createElement('tr');
            newBookTr.innerHTML += `<td>${json[key].title}</td><td>${json[key].author}</td>`;

            let functionalTd = document.createElement('td');

            let editButton = document.createElement('button');
            editButton.textContent = 'Edit';
            editButton.addEventListener('click', async () => {
                currentId = key;
                await getRequestEditBook();
            });

            let deleteButton = document.createElement('button');
            deleteButton.textContent = 'Delete';
            deleteButton.addEventListener('click', async () => await deleteBook(key));

            functionalTd.appendChild(editButton);
            functionalTd.appendChild(deleteButton);

            newBookTr.appendChild(functionalTd);

            booksTBody.appendChild(newBookTr);
        })
}

async function addBook(e) {
    e.preventDefault();
    let formData = new FormData(e.target);
    const author = formData.get('author');
    const title = formData.get('title');

    if (!author || !title)
        return alert('Invalid form.')
    await fetch(`http://localhost:3030/jsonstore/collections/books`, {
        method: 'POST',
        body: JSON.stringify({author, title})
    });

    bookTitleField.value = '';
    bookAuthorField.value = '';

    await getBooks();
}

async function getRequestEditBook() {
    let response = await fetch(`http://localhost:3030/jsonstore/collections/books/${currentId}`);
    let json = await response.json();

    bookForm.querySelector('h3').textContent = 'Edit FORM';
    bookForm.querySelector('[name="title"]').value = json.title;
    bookForm.querySelector('[name="author"]').value = json.author;

    bookForm.querySelector('button').remove();

    let saveButton = document.createElement('button');
    saveButton.textContent = 'Save';

    bookForm.appendChild(saveButton);

    bookForm.removeEventListener('submit', addBook);
    bookForm.addEventListener('submit', postRequestEditBook);
}

async function postRequestEditBook(e) {
    e.preventDefault();
    let formData = new FormData(e.target);
    const author = formData.get('author');
    const title = formData.get('title');

    await fetch(`http://localhost:3030/jsonstore/collections/books/${currentId}`, {
        method: 'PUT',
        body: JSON.stringify({author, title})
    })

    currentId = null;

    bookForm.querySelector('h3').textContent = 'FORM';
    bookForm.querySelector('button').remove();
    bookForm.removeEventListener('submit', postRequestEditBook);
    bookForm.addEventListener('submit', addBook);

    let submitButton = document.createElement('button');
    submitButton.textContent = 'Submit';
    bookForm.appendChild(submitButton);

    bookTitleField.value = '';
    bookAuthorField.value = '';

    await getBooks();
}

async function deleteBook(id) {
    await fetch(`http://localhost:3030/jsonstore/collections/books/${id}`, {
        method: 'DELETE'
    })
    await getBooks();
}