const textArea = document.getElementById('messages');
const refreshButton = document.getElementById('refresh');
const submitButton = document.getElementById('submit');

const authorField = document.getElementById('author');
const contentField = document.getElementById('content');

refreshButton.addEventListener('click', refreshMessages);
submitButton.addEventListener('click', postMessage);

async function refreshMessages() {
    let response = await fetch(`http://localhost:3030/jsonstore/messenger`);
    let content = Object.values((await response.json()))
        .map(e => `${e.author}: ${e.content}`);
    textArea.textContent = content.join('\n');
}

async function postMessage() {
    if (!authorField.value || !contentField.value)
        return alert('Invalid message!');
    
    await fetch(`http://localhost:3030/jsonstore/messenger`, {
        method: 'POST',
        body: JSON.stringify({author: authorField.value, content: contentField.value})
    });

    authorField.value = '';
    contentField.value = '';
    await refreshMessages();
}

refreshMessages();