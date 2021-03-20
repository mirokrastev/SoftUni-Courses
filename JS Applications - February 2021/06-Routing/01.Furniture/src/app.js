import page from "//unpkg.com/page/page.mjs";
import {setupNavbar} from "./navbar.js";
import {homeView} from "./home/home.js";
import {loginView} from "./auth/login.js";
import {registerView} from "./auth/register.js";
import {detailsView} from "./crud/details.js";
import {createView} from "./crud/create.js";
import {publicationsView} from "./home/my-furnitures.js";
import {editView} from "./crud/edit.js";

setupNavbar(location.pathname);

page('/', homeView);
page('/login', loginView);
page('/register', registerView);
page('/create', createView);
page('/my-furniture', publicationsView);
page('/details/:id', detailsView);
page('/edit/:id', editView);

page.start();