import {addMovie, showAddMovie} from "./movies.js";
import {main} from "./app.js";

const allSections = {
    'home-page': document.getElementById('home-page'),
    'add-movie-button': document.getElementById('add-movie-button'),
    'movie': document.getElementById('movie'),
    'add-movie': document.getElementById('add-movie'),
    'movie-example': document.getElementById('movie-example'),
    'edit-movie': document.getElementById('edit-movie'),
    'form-login': document.getElementById('form-login'),
    'form-sign-up': document.getElementById('form-sign-up'),
    'moviesHTag': document.getElementById('moviesHTag')
}

allSections['add-movie-button']
    .addEventListener('click', showAddMovie)

allSections['add-movie'].querySelector('form')
    .addEventListener('submit', addMovie)

document.querySelector('#homePageBtn')
    .addEventListener('click', main);

function hide(...el) {
    el.forEach(e => allSections[e].style.display = 'none');
}

function show(...el) {
    el.forEach(e => allSections[e].style.display = 'block');
}


export {
    hide,
    show
}