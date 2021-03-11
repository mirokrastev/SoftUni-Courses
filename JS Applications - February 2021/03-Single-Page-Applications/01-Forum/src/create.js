import { showPost } from './post.js'

let form;

function setupCreate(formEl) {
    form = formEl;
    document.querySelector('.cancel')
        .addEventListener('click', (e) => {
            e.preventDefault();
            e.stopImmediatePropagation();
            [...form].forEach(e => e.value = '');
        })
    form.addEventListener('submit', onSubmit)
}

async function onSubmit(e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    const formDataObj = [...formData.entries()]
        .reduce((p, [k, v]) => Object.assign(p, {[k]: v}), {})

    let response = await fetch('http://localhost:3030/jsonstore/collections/myboard/posts', {
        method: 'POST'
    });

    let data = await response.json();

    await fetch(`http://localhost:3030/jsonstore/collections/myboard/posts/${data._id}`, {
        method: 'PUT',
        body: JSON.stringify({...formDataObj})
    });
    [...form].forEach(e => e.value = '');
    await showPost();
}

export {
    setupCreate,
    onSubmit
}