import { setupNavbar, changeNavbar } from './navbar.js'
import { setupLogin } from './login.js'
import { setupRegister } from './register.js';
import {setupMovies, showMovies} from './movies.js'
import { show, hide } from './common.js';

const authToken = sessionStorage.getItem('authToken');
const userId = sessionStorage.getItem('userId');

export async function main() {
    setupNavbar(document.querySelector('nav'));
    changeNavbar();

    setupLogin(document.querySelector('#form-login'));
    setupRegister(document.querySelector('#form-sign-up'));

    setupMovies(document.querySelector('#movie'));
    hide('edit-movie', 'movie-example', 'add-movie');
    show('movie', 'home-page');
    if (authToken) {
        await showMovies();
        show( 'add-movie-button');
    }
    else {
        await showMovies();
        hide('add-movie-button');
    }
}

main();