import * as login from './login.js'
import * as register from './register.js'

const authToken = sessionStorage.getItem('authToken');
const userId = sessionStorage.getItem('userId');
const userEmail = sessionStorage.getItem('userEmail');
let userObj;

let navbar;

function setupNavbar(nav) {
    navbar = nav;
}

function changeNavbar() {
    document.querySelector('#logout')
        .addEventListener('click', () => {
            sessionStorage.removeItem('authToken');
            sessionStorage.removeItem('userId');
            sessionStorage.removeItem('userEmail');

            window.location.pathname = '';
        })
    const navbarElements =   [...navbar.querySelectorAll('li')]
    if (authToken === null) {
        navbarElements
            .slice(0, 2).forEach(node => node.style.display = 'none');

        navbarElements
            .slice(2).forEach(node => node.style.display = 'inline-block');

        navbar.querySelector('#login')
            .addEventListener('click', login.showLogin);
        navbar.querySelector('#register')
            .addEventListener('click', register.showRegister);
    }
    else {
        navbarElements
            .slice(2).forEach(node => node.style.display = 'none');

        navbarElements
            .slice(0, 2).forEach(node => node.style.display = 'inline-block');

        navbar.querySelector('#welcome')
            .textContent = `Welcome, ${userEmail}`;
    }
}

export {
    setupNavbar,
    changeNavbar
}