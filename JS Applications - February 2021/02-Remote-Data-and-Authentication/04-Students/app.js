const resultTBody = document.getElementById('resultTBody');
const form = document.getElementById('studentForm');
const flowOrder = ['id', 'firstName', 'lastName', 'facultyNumber', 'grade']

form.addEventListener('submit', addStudent);

async function getStudents() {
    let response = await fetch(`http://localhost:3030/jsonstore/collections/students`);
    let json = await response.json();
    resultTBody.innerHTML = '';
    let id = 1;

    Object.values(json)
        .forEach(obj => {
            let newTr = document.createElement('tr');
            flowOrder.forEach(e => {
                if (e === 'id') {
                    newTr.innerHTML += `<td>${id}</td>`
                    id++
                    return;
                }
                newTr.innerHTML += `<td>${obj[e]}</td>`;
            });
            resultTBody.appendChild(newTr);
        });

    sortObjects();
}

async function addStudent(e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    const id = formData.get('id');
    const firstName = formData.get('firstName');
    const lastName = formData.get('lastName');
    const facultyNumber = formData.get('facultyNumber');
    const grade = formData.get('grade');

    if (!id || !firstName ||!lastName || !facultyNumber || !grade)
        return alert('Invalid form.')

    await fetch(`http://localhost:3030/jsonstore/collections/students`, {
        method: 'POST',
        body: JSON.stringify({id, firstName, lastName, facultyNumber, grade})
    });
    await getStudents();
}

function sortObjects() {
    Array.from(resultTBody.children)
        .sort((a, b) => Number(a.cells[0].textContent) - Number(b.cells[0].textContent))
        .forEach(node => resultTBody.appendChild(node));
}

getStudents();