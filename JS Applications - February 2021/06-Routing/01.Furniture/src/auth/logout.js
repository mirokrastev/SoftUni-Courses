import page from "//unpkg.com/page/page.mjs";
import {checkAuth} from "./checkAuth.js";

export async function logoutUser() {
    checkAuth();

    await fetch('http://localhost:3000/users/logout');
    sessionStorage.clear();
    page.redirect('/')
}