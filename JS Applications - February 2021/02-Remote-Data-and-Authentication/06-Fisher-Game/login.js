const signInForm = document.getElementById('signup');
signInForm.addEventListener('submit', registerUser);

const loginForm = document.getElementById('signin');
loginForm.addEventListener('submit', loginUser);


async function registerUser(e) {
    e.preventDefault();

    let formData = new FormData(e.target);
    const email = formData.get('email');
    const password = formData.get('password');
    const rePass = formData.get('rePass');

    if (password !== rePass)
        return alert('Password doesn\'t match!');

    let response = await fetch(`http://localhost:3030/users/register`, {
        method: 'POST',
        body: JSON.stringify({email, password})
    });

    let data = await response.json();

    if (response.ok) {
        sessionStorage.setItem('authToken', data.accessToken);
        sessionStorage.setItem('userId', data._id);
        window.location.pathname = '06.Fisher-Game/index.html';
    }
    else {
        return alert('Invalid form!');
    }
}

async function loginUser(e) {
    e.preventDefault();

    let formData = new FormData(e.target);
    const email = formData.get('email');
    const password = formData.get('password');

    let response = await fetch(`http://localhost:3030/users/login`, {
        method: 'POST',
        body: JSON.stringify({email, password})
    });
    let data = await response.json();

    if (response.ok) {
        console.log(data);
        sessionStorage.setItem('authToken', data.accessToken);
        sessionStorage.setItem('userId', data._id);
        window.location.pathname = '06.Fisher-Game/index.html';
    }
    else {
        return alert('Invalid credentials!');
    }
}