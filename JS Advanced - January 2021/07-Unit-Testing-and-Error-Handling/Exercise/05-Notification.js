function notify(message) {
    let divNotification = document.getElementById('notification');
    divNotification.addEventListener('click', () => {
        divNotification.style.display = 'none';
    })

    divNotification.textContent = message;
    divNotification.style.display = "block";
}