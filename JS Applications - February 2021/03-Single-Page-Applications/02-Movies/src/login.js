import * as common from './common.js'
import {main} from "./app.js";

let form;

function setupLogin(loginForm) {
    form = loginForm;
    form.style.display = 'none';
    form.querySelector('form')
        .addEventListener('submit', loginUser);
}

async function showLogin() {
    form.style.display = 'block';
    common.hide('home-page', 'add-movie-button', 'movie', 'add-movie',
        'movie-example', 'edit-movie', 'form-sign-up')
}

async function loginUser(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const email = formData.get('email');
    const password = formData.get('password');

    let response = await fetch('http://localhost:3030/users/login', {
        method: 'POST',
        body: JSON.stringify({email, password})
    });

    if (!response.ok) {
        [...form.querySelector('form')]
            .forEach(e => e.value = '');
        return alert('Invalid Form.');
    }
    let data = await response.json();
    sessionStorage.setItem('authToken', data.accessToken);
    sessionStorage.setItem('userId', data._id);
    sessionStorage.setItem('userEmail', data.email);

    window.location.pathname = '';
}

export {
    setupLogin,
    showLogin,
    loginUser
}