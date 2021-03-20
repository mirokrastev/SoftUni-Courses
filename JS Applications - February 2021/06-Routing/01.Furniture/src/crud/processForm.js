import page from "//unpkg.com/page/page.mjs";

export async function processForm(e, ...args) {
    e.preventDefault();

    const authToken = sessionStorage.getItem('authToken');

    const make = e.target.querySelector('#new-make');
    const price =  e.target.querySelector('#new-price');
    const model =  e.target.querySelector('#new-model');
    const img =  e.target.querySelector('#new-image');
    const year =  e.target.querySelector('#new-year');
    const description =  e.target.querySelector('#new-description');
    const material =  e.target.querySelector('#new-material');

    let valid = true;

    if (!make.value || make.value.length < 4) {
        make.className = 'form-control is-invalid'
        valid = false;
    }
    else {
        make.className = 'form-control is-valid';
    }

    if (!price.value || Number(price) < 0) {
        price.className = 'form-control is-invalid';
        valid = false;
    }
    else {
        price.className = 'form-control is-valid';
    }

    if (!description.value || description.value.length < 10) {
        description.className = 'form-control is-invalid';
        valid = false;
    }
    else {
        description.className = 'form-control is-valid';
    }

    if (!model.value || model.length < 4) {
        model.className = 'form-control is-invalid';
        valid = false;
    }
    else {
        model.className = 'form-control is-valid';
    }

    if (!img.value) {
        img.className = 'form-control is-invalid';
        valid = false;
    }
    else {
        img.className = 'form-control is-valid';
    }

    if (!year.value || Number(year.value) < 1950 || Number(year.value) > 2050) {
        year.className = 'form-control is-invalid';
        valid = false;
    }
    else {
        year.className = 'form-control is-valid';
    }

    if (!valid) {
        return alert('Invalid form.');
    }

    async function postRequest() {
        const response = await fetch('http://localhost:3030/data/catalog', {
            method: 'POST',
            headers: {'X-Authorization': authToken},
            body: JSON.stringify({
                make: make.value, price: Number(price.value),
                model: model.value, img: img.value, year: year.value, description: description.value,
                material: material.value
            })
        });

        if (!response.ok) {
            return alert('Suspicious operation.');
        }
        page.redirect('/');
    }

    async function putRequest(id) {
        const response = await fetch(`http://localhost:3030/data/catalog/${id}`, {
            method: 'PUT',
            headers: {'X-Authorization': authToken},
            body: JSON.stringify({
                make: make.value, price: Number(price.value),
                model: model.value, img: img.value, year: year.value, description: description.value,
                material: material.value
            })
        });

        if (!response.ok) {
            return alert('Suspicious operation.');
        }
        page.redirect('/')
    }

    const mapper = {
        'post': postRequest,
        'put': putRequest
    }

    let [request, id] = args;
    mapper[request](id);
}