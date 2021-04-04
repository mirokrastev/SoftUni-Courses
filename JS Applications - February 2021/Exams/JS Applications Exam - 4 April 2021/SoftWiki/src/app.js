import page from '../node_modules/page/page.mjs';
import {html, render} from '../node_modules/lit-html/lit-html.js';
import {setupNavbar} from './navbar.js';
import {catalogueView, homeView} from "./home.js";
import {loginView} from "./auth/login.js";
import {registerView} from "./auth/register.js";
import {createView} from "./crud/create.js";
import {detailedView} from "./crud/detailed.js";
import {editView} from "./crud/edit.js";
import {searchTopicView} from "./search.js";

setupNavbar();

page('/', homeView);
page('/catalogue', catalogueView);
page('/search', searchTopicView);
page('/login', loginView);
page('/register', registerView);
page('/create', createView);
page('/details/:id', detailedView);
page('/edit/:id', editView);

page.start();