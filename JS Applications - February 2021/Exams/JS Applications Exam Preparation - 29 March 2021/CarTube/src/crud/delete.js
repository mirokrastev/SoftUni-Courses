import {html, render} from '../../node_modules/lit-html/lit-html.js';
import page from '../../node_modules/page/page.mjs';
import apiReq from "../api/request.js";

const api = apiReq();

export async function deleteFunc(id) {
    const confirmAction = confirm('Are you sure you want to delete this offer?')
    if (!confirmAction) {
        return;
    }

    try {
        const result = await api._delete(`data/cars/` + id, null, true)
        page.redirect('/all-listings');
    }
    catch (e) {
        return alert(e.message);
    }
}