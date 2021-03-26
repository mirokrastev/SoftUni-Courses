import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import apiReq from "../api/request.js";

const api = apiReq();

export async function deleteFunc(id) {
    try {
        const result = await api._delete(`data/articles/` + id, null, true)
        page.redirect('/');
    }
    catch (e) {
        return alert(e.message);
    }
}