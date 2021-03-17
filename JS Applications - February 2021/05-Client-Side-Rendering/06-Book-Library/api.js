export function processForm(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const title = formData.get('title');
    const author = formData.get('author');

    if (!title || !author)
        return alert('Invalid form.');
    [...e.target]
        .forEach(e => {
            if (e.type !== 'submit')
                e.value = '';
        });
    return [author, title]
}