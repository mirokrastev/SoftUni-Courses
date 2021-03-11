import { hide, show } from "./common.js";
import { e } from "./dom.js";
import {main} from "./app.js";

let section;

const authToken = sessionStorage.getItem('authToken');
const userId = sessionStorage.getItem('userId');

async function getMovies() {
    let response = await fetch('http://localhost:3030/data/movies');
    return await response.json();
}

function setupMovies(sectionEl) {
    if (authToken === null) {
        hide('add-movie-button');
    }
    if (sectionEl === 'hide') {
        section.style.display = 'none';
        document.querySelector('h1.text-center').style.display = 'none';
        hide('add-movie-button');
    }
    else if (sectionEl === 'show') {
        sectionEl.style.dispaly = 'block';
        document.querySelector('h1.text-center').style.display = 'block';
        show('add-movie-button');
    }
    else {
        section = sectionEl;
    }
}

async function showMovies() {
    let movies = await getMovies();
    const mainMoviesEl = document.querySelector('#mainMovies');
    const fragment = document.createDocumentFragment();
    mainMoviesEl.innerHTML = '';
    movies.forEach(movie => {
        fragment.appendChild(e('div', {className: 'card mb-4'},
            e('img', {className: 'card-img-top', src: movie.img, alt: 'Card image cap', width: '400'}),
            e('div', {className: 'card-body'},
                e('a', {href: 'javascript:void(0)'},
                    e('button', {type: 'button', className: 'btn btn-info',
                        onClick: () => detailedMovie(movie._id)}, 'Details')))))
    })
    if (authToken === null) {
        fragment.querySelectorAll('a')
            .forEach(node => node.remove());
    }
    mainMoviesEl.appendChild(fragment);
}

async function detailedMovie(id) {
    const response = await fetch(`http://localhost:3030/data/movies/${id}`);
    const data = await response.json();

    const divEl = document.querySelector('#movieExampleDiv');
    divEl.innerHTML = '';

    const fragment = document.createDocumentFragment();
    fragment.appendChild(e('h1', {}, `Movie title: ${data.title}`))
    fragment.appendChild(e('div', {className: 'col-md-8'},
        e('img', {className: 'img-thumbnail', src: data.img})));
    fragment.appendChild(e('div', {className: 'col-md-4 text-center'},
        e('h3', {className: 'my-3'}, 'Movie Description'),
        e('p', {}, data.description),
        e('a', {className: 'btn btn-danger',
                        href: 'javascript:void(0)', onClick: async () => {
            await fetch(`http://localhost:3030/data/movies/${data._id}`, {
                method: 'DELETE',
                headers: {'X-Authorization': authToken}
            });
            return await main();
                }},
            'Delete')));

    if (data._ownerId !== userId) {
        fragment.querySelector('a').remove();
    }

    document.querySelector('#movieExampleDiv')
        .appendChild(fragment);
    hide('home-page', 'add-movie-button', 'movie', 'add-movie', 'edit-movie',
        'form-login', 'form-sign-up', 'moviesHTag');
    show('movie-example');
}

function showAddMovie() {
    hide('home-page', 'add-movie-button', 'movie', 'movie-example',
        'edit-movie', 'form-login', 'form-sign-up', 'moviesHTag');
    show('add-movie');
}

async function addMovie(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const title = formData.get('title');
    const description = formData.get('description');
    const imageUrl = formData.get('imageUrl');

    if (!title || !description || !imageUrl) {
        [...e.target]
            .forEach(node => node.value = '');
        return alert('Invalid Form.');
    }

    let response = await fetch('http://localhost:3030/data/movies', {
        method: 'POST',
        headers: {'Content-Type': 'application/json', 'X-Authorization': authToken},
        body: JSON.stringify({title, description, imageUrl})
    });

    if (!response.ok) {
        console.log(response);
        [...e.target]
            .forEach(node => node.value = '');
        return alert('Invalid Request.');
    }
    return await main();
}

export {
    setupMovies,
    showMovies,
    showAddMovie,
    addMovie
}