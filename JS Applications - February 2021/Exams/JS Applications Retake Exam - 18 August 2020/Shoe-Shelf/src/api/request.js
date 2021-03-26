import {FormDataPairs} from './data.js';
import page from '../../node_modules/page/page.mjs';

export default function apiReq() {
    const HOST = 'http://localhost:3030'

    return {
        async request(endpoint, options) {

            try {
                const response = await fetch(endpoint, options);

                if (response.ok) {
                    return await response.json();
                }
                else {
                    const error = await response.json();
                    throw new Error(error.message);
                }
            }
            catch (error) {
                if (error === 'Invalid access token') {
                    alert('Invalid session, resetting storage');
                    sessionStorage.clear();
                    page.redirect('/');
                }
                else {
                    throw new Error(error.message);
                }
            }
        },

        getHeaders() {
            const headers = {};
            const authToken = sessionStorage.getItem('authToken');

            if (authToken)
                headers['X-Authorization'] = authToken;
            else
                throw new Error('No access token.')
            return headers;
        },

        async get(partialEndpoint, auth = false) {
            const endpoint = `${HOST}/${partialEndpoint}`;
            const options = {method: 'GET'};

            if (auth)
                options.headers = this.getHeaders();

            try {
                return await this.request(endpoint, options);
            } catch (e) {
                throw new Error(e.message);
            }
        },

        async post(partialEndpoint, body=null, auth = false) {
            const endpoint = `${HOST}/${partialEndpoint}`;
            const options = {method: 'POST'};

            if (body) {
                options.body = JSON.stringify(body);
            }
            if (auth)
                options.headers = this.getHeaders();

            try {
                return await this.request(endpoint, options);
            } catch (e) {
                throw new Error(e.message);
            }
        },

        async put(partialEndpoint, body=null, auth = false) {
            const endpoint = `${HOST}/${partialEndpoint}`;
            const options = {method:'PUT'}

            if (body) {
                options.body = JSON.stringify(body);
            }
            if (auth)
                options.headers = this.getHeaders();

            try {
                return await this.request(endpoint, options);
            } catch (e) {
                throw new Error(e.message);
            }
        },

        async _delete(partialEndpoint, body=null, auth = false) {
            const endpoint = `${HOST}/${partialEndpoint}`
            const options = {method: 'DELETE'};

            if (body) {
                options.body = JSON.stringify(body);
            }
            if (auth)
                options.headers = this.getHeaders();
            try {
                return await this.request(endpoint, options);
            } catch (e) {
                throw new Error(e.message);
            }
        },

        async login(formData, ...exclude) {
            const body = FormDataPairs(formData, ...exclude);
            const endpoint = `users/login`;

            try {
                const data = await this.post(endpoint, body);
                sessionStorage.setItem('authToken', data.accessToken);
                sessionStorage.setItem('userId', data._id);
                sessionStorage.setItem('userEmail', data.email);
                return data;
            } catch (e) {
                throw new Error(e.message);
            }
        },

        async register(formData) {
            const data = FormDataPairs(formData);

            const body = {email: data['email'], password: data['password']};
            const endpoint = `users/register`;

            try {
                const data = await this.post(endpoint, body);
                sessionStorage.setItem('authToken', data.accessToken);
                sessionStorage.setItem('userId', data._id);
                sessionStorage.setItem('userEmail', data.email);
                return data;
            }
            catch (e) {
                throw new Error(e.message);
            }
        },
        async logout() {
            const authToken = sessionStorage.getItem('authToken');
            await fetch(`${HOST}/users/logout`, {
                method: 'GET',
                headers: {'X-Authorization': authToken}
            });
            sessionStorage.clear();
        }
    }
}