const loadPostsButton = document.getElementById('btnLoadPosts');
loadPostsButton.addEventListener('click', loadPosts)

const postsMenu = document.getElementById('posts');

const viewPostButton = document.getElementById('btnViewPost');
viewPostButton.addEventListener('click', viewPost)

function loadPosts() {
    fetch('http://localhost:3030/jsonstore/blog/posts')
        .then(response => response.json())
        .then(data => {
            Object.values(data)
                .forEach(e => createPost(e));
        })
}

function createPost(object) {
    postsMenu.innerHTML += `
    <option value="${object.id}">${object.title.toUpperCase()}</option>
    `;
}

function viewPost() {
    let postId = postsMenu.value;
    if(!postId)
        return;

    fetch(`http://localhost:3030/jsonstore/blog/comments`)
        .then(response => response.json())
        .then(data => {
            let posts = Object.values(data)
                          .filter(e => e.postId === postId);

            fetch(`http://localhost:3030/jsonstore/blog/posts/${postId}`)
                .then(response => response.json())
                .then(data => {
                    document.querySelector('#post-title').textContent = data.title;
                    document.querySelector('#post-body').textContent = data.body;
                });

            document.querySelector('#post-comments').innerHTML = posts.map(e => `<li>${e.text}</li>`).join('');
        })
}