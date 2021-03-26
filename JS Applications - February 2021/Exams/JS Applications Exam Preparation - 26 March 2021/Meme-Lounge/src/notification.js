import {html, render} from '../node_modules/lit-html/lit-html.js';
import {styleMap} from '../node_modules/lit-html/directives/style-map.js';

const notification = document.getElementById('mainNotification');

export function clearNotification() {
    render(html``, notification);
}

export function makeNotification(error) {
    const template = html`
            <section id="notifications">
                <div style=${styleMap({'display': 'inline-block'})} id="errorBox" class="notification">
                    <span>${error}</span>
                </div>
            </section>`;
    render(template, notification);

    setTimeout(() => {
        clearNotification();
    }, 3000);
}