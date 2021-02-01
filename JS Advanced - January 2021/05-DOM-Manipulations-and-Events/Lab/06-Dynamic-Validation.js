function validate() {
    let inputField = document.getElementById('email');
    inputField.addEventListener('change', onChangeField)
    let rePattern = /[a-z]+@[a-z]+\.[a-z]+/g

    function onChangeField(event) {
        let newText = event.target.value.match(rePattern);
        if (newText === null) {
            event.target.setAttribute('class', 'error');
        }
        else {
            event.target.removeAttribute('class');
        }
    }
}