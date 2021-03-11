import { e } from './dom.js'
import * as detail from './details.js'

let section;

function setupPost(sectionEl) {
    section = sectionEl;
}

async function showPost() {
    section.innerHTML = 'Loading...';

    const posts = await getPosts();
    const cards = Object.values(posts).map(createPostDOM)

    const fragment = document.createDocumentFragment();
    cards.forEach(c => fragment.appendChild(c));
    section.innerHTML = '';
    section.appendChild(fragment);
}

async function getPosts() {
    let response = await fetch('http://localhost:3030/jsonstore/collections/myboard/posts');
    return await response.json();
}

function createPostDOM(postObj) {
    const result = e('div', {className: 'topic-container', onClick: () => detail.showDetails(postObj._id)},
        e('div', {className: 'topic-name-wrapper'},
            e('div', {className: 'topic-name'},
                e('a', {href: 'javascript:void(0)', className: 'normal'},
                    e('h2', {}, postObj.topicName)),
                e('div', {className: 'columns'},
                    e('div', {},
                        e('p', {}, `Date: `,
                            e('time', {}, 'Not specified')),
                        e('div', {className: 'nick-name'},
                            e('p', {},
                                e('span', {}, `Username: ${postObj.username}`)))),
                    e('div', {className: 'subscribers'},
                        e('p', {}, 'Subscribers: ',
                            e('span', {}, 'Not specified')))))));
    return result;
}

export {
    setupPost,
    showPost
}