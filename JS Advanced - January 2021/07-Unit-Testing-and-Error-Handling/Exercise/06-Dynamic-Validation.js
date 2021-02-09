function validate() {
    let regexPattern = /([a-z]+)@([a-z]+)\.([a-z]+)/g;
    let inputField = document.getElementById('email');
    inputField.addEventListener('change', () => {
        if (!inputField.value.match(regexPattern)) {
            inputField.setAttribute('class', 'error');
        }
        else {
            inputField.removeAttribute('class');
        }
    })
}