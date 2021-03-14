import {main} from "./app.js";

const formTypeDict = {
    'login': ['http://localhost:3030/users/login', {method: 'POST'}],
    'register': ['http://localhost:3030/users/register', {method: 'POST'}]
}

export async function authFormAPI(e, type) {
    e.preventDefault();
    let [url, props] = formTypeDict[type];
    const formData = new FormData(e.target);
    let pairs = [...formData.entries()]
        .reduce((p, [k, v]) => Object.assign(p, {[k]: v}), {})

    if (type === 'login') {
        props = {...props, body: JSON.stringify(pairs)}
    }
    else if (type === 'register') {
        pairs = {email: formData.get('email'), password: formData.get('password')}
        props = {...props, body: JSON.stringify(pairs)}
    }

    const response = await fetch(url, props);
    if (!response.ok) {
        [...e.target]
            .forEach(e => {
                if (e.tagName === 'INPUT') {
                    e.value = '';
                }
            });
        return alert('Invalid form.');
    }

    const data = await response.json();
    await sessionStorage.setItem('authToken', data.accessToken);
    await sessionStorage.setItem('userId', data._id);
    return await main();
}