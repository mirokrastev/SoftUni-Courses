import * as common from "./common.js";
import { main } from './app.js'

let form;

function setupRegister(registerForm) {
    form = registerForm;
    form.style.display = 'none';
    form.addEventListener('submit', registerUser);
}

async function showRegister() {
    form.style.display = 'block';
    common.hide('home-page', 'add-movie-button', 'movie', 'add-movie',
        'movie-example', 'edit-movie', 'form-login');
}

async function registerUser(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const email = formData.get('email');
    const password = formData.get('password');
    const rePass = formData.get('repeatPassword');
    if (!email || password.length < 6 || password !== rePass) {
        [...form.querySelector('form')]
            .forEach(e => e.value = '');
        return alert('Invalid credentials.');
    }

    let response = await fetch('http://localhost:3030/users/register', {
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

    window.location.pathname = '02.Movies/index.html';
}

export {
    setupRegister,
    showRegister,
    registerUser
}