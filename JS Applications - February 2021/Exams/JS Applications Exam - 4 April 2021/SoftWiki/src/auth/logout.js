import page from '../../node_modules/page/page.mjs';
import {html, render} from '../../node_modules/lit-html/lit-html.js';
import apiReq from "../api/request.js";

const api = apiReq();

export async function logoutUser() {
    await api.logout()
    page.redirect('/');
}