import page from "//unpkg.com/page/page.mjs";

export async function deleteObject(object) {
    const authToken = sessionStorage.getItem('authToken');

    const confirmWindow = confirm('Are you sure you want to delete this item?');
    if (!confirmWindow) {
        return page.redirect('/')
    }

    const response = await fetch(`http://localhost:3030/data/catalog/${object._id}`, {
        method: 'DELETE',
        headers: {'X-Authorization': authToken}
    });

    if (!response.ok) {
        return alert('Suspicious operation.');
    }

    page.redirect('/');
}