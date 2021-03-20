import page from "//unpkg.com/page/page.mjs";

export function checkAuth() {
    const userId = sessionStorage.getItem('userId');

    if (!userId) {
        alert('Suspicious operation.');
        return page.redirect('/');
    }
}