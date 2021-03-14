import {main} from "../app.js";

export async function logoutView() {
    const authToken = sessionStorage.getItem('authToken');

    const response = await fetch('http://localhost:3030/users/logout', {
        method: 'GET',
        headers: {'X-Authorization': authToken}
    });
    if (!response.ok) {
        return alert('Suspicious operation.');
    }

    sessionStorage.clear();
    return main();
}