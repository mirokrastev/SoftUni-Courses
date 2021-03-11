import { e } from './dom.js'

let main;
let id;

async function getPostById(id) {
    let response = await fetch(`http://localhost:3030/jsonstore/collections/myboard/posts/${id}`);
    return await response.json();
}

function createPostDetailsDOM(postObj) {
    const postDOM = e('div', {className: 'topic-content'},
        e('div', {classname: 'topic-title'},
            e('div', {classname: 'topic-name-wrapper'},
                e('div', {className: 'topic-name'},
                    e('h2', {}, postObj.topicName),
                    e('p', {}, 'Date: ',
                        e('time', {}, 'Not specified'))))));
    return postDOM;
}

function createPostCommentsDOM(commentObj) {
    let commentDOM = e('div', {className: 'comment'},
        e('header', {className: 'header'},
            e('p', {},
                e('span', {}, commentObj.username),
                ' Posted on ',
                e('time', {}, 'Not specified'))),
        e('div', {className: 'comment-main'},
            e('div', {className: 'userdetails'},
                e('img', {src: './static/profile.png', alt: 'avatar'})),
            e('div', {className: 'post-content'},
                e('p', {}, commentObj.postText))));
    return commentDOM;
}

function createCommentDOM() {
    const commentForm = e('div', {className: 'answer-comment'},
        e('p', {},
            e('span', {}, 'CurrentUser',
                e('span', {}, ' comment:')),
            e('div', {className: 'answer'},
                e('form', {id: 'commentForm', onSubmit: submitComment},
                    e('textarea', {name:'postText', id: 'comment', cols: 30, rows: 10}),
                    e('div', {},
                        e('label', {for: 'username'}, 'Username ',
                            e('span', {className: 'red'}, '*')),
                        e('input', {type: 'text', name: 'username', id: 'username'}),
                        e('button', {}, 'Post'))))));
    return commentForm;
}

async function submitComment(e) {
    e.preventDefault();
    let formData = new FormData(e.target);
    const formDataObj = [...formData.entries()]
        .reduce((p, [k, v]) => Object.assign(p, {[k]: v}), {})

    let response = await fetch('http://localhost:3030/jsonstore/collections/myboard/comments', {
        method: 'POST'
    });

    let data = await response.json();

    await fetch(`http://localhost:3030/jsonstore/collections/myboard/comments/${data._id}`, {
        method: 'PUT',
        body: JSON.stringify({...formDataObj, postId: id})
    });
    [...document.querySelector('form')]
        .forEach(e => e.value = '');
    await showDetails(id);
}

function setupDetails(mainEl) {
    main = mainEl;
}

async function showDetails(outerId) {
    id = outerId;
    main.innerHTML = 'Loading...';
    const post = createPostDetailsDOM(await getPostById(id));
    main.innerHTML = '';
    main.appendChild(post);

    let response = await fetch(`http://localhost:3030/jsonstore/collections/myboard/comments`);
    let data = Object.values(await response.json());

    let allComments = data.filter(obj => obj.postId === id);
    if (allComments.length > 0) {
        const fragment = document.createDocumentFragment();
        allComments.map(e => createPostCommentsDOM(e))
            .forEach(e => fragment.appendChild(e));
        document.querySelector('.topic-content').appendChild(fragment);
    }
    let commentForm = createCommentDOM();
    document.querySelector('.topic-content').appendChild(commentForm);
}

export {
    setupDetails,
    showDetails
}