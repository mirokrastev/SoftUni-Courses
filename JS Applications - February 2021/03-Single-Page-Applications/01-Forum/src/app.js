import * as post from './post.js'
import * as create from './create.js'
import * as detail from './details.js'

main();

async function main() {
    create.setupCreate(document.querySelector('#newTopic'));
    detail.setupDetails(document.querySelector('.container'))
    post.setupPost(document.querySelector('.topic-title'));
    await post.showPost();
}