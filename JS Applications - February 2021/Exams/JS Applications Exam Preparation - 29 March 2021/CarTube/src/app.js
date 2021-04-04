import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import {setupNavbar} from './navbar.js';
import {homeView} from "./home.js";
import {loginView} from "./auth/login.js";
import {registerView} from "./auth/register.js";
import {createView} from "./crud/create.js";
import {detailedView} from "./crud/detailed.js";
import {editView} from "./crud/edit.js";
import {allListingsView} from "./all-listings.js";
import {myListingsView} from "./my-listings.js";
import {searchListingsView} from "./search-listings.js";

setupNavbar();

page('/', homeView);
page('/all-listings', allListingsView);
page('/my-listings', myListingsView);
page('/search', searchListingsView);
page('/login', loginView);
page('/register', registerView);
page('/create', createView);
page('/details/:id', detailedView);
page('/edit/:id', editView);

page.start();