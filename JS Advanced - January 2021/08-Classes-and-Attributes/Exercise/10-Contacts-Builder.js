class Contact {
    constructor(firstName, lastName, phone, email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.phone = phone;
        this.email = email;
        this.online = false;
        this.reference = null;
        this.lastBlock = null;
    }

    get online() {
        return this._online;
    }

    set online(value) {
        let mapper = {
            true: 'title online',
            false: 'title'
        }
        if (this.reference) {
            this.reference.firstChild.className = mapper[value];
        }
        this._online = value;
    }

    render(id) {
        let elementToRender = document.getElementById(id);

        let newArticle = document.createElement('article');
        let nameDivEl = document.createElement('div');
        if (this.online) {
            nameDivEl.className = 'title online';
        } else {
            nameDivEl.className = 'title';
        }
        nameDivEl.innerHTML += `${this.firstName} ${this.lastName}`;

        let additionalInfoButton = document.createElement('button');
        additionalInfoButton.innerHTML = '&#8505';
        additionalInfoButton.addEventListener('click', () => {
            let mapper = {
                'block': 'none',
                'none': 'block'
            }
            let call = mapper[this.lastBlock]
            infoDivEl.style.display = call;
            this.lastBlock = call;
        })

        nameDivEl.appendChild(additionalInfoButton);

        newArticle.appendChild(nameDivEl);

        let infoDivEl = document.createElement('div');
        infoDivEl.className = 'info'
        infoDivEl.style.display = 'none';
        this.lastBlock = 'none';
        infoDivEl.innerHTML += `<span>&phone; ${this.phone}</span><span>&#9993; ${this.email}</span>`;

        newArticle.appendChild(infoDivEl);

        elementToRender.appendChild(newArticle);

        this.reference = newArticle;
    }
}