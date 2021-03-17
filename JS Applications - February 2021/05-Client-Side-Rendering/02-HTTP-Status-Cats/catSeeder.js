class Cat {
    constructor(id, statusCode, statusMessage, imageLocation) {
        this.id = id;
        this.statusCode = statusCode;
        this.statusMessage = statusMessage;
        this.imageLocation = imageLocation;
    }
}

const cats = [
    new Cat('100', 100, 'Continue', './images/cat100.jpg'),
    new Cat('200', 200, 'Ok', './images/cat200.jpg'),
    new Cat('204', 204, 'No content', './images/cat204.jpg'),
    new Cat('301', 301, 'Moved permanently', './images/cat301.jpg'),
    new Cat('304', 304, 'Not modified', './images/cat304.jpg'),
    new Cat('400', 400, 'Bad request', './images/cat400.jpg'),
    new Cat('404', 404, 'Not Found', './images/cat404.jpg'),
    new Cat('406', 406, 'Not Acceptable', './images/cat406.jpg'),
    new Cat('410', 410, 'Gone', './images/cat410.jpg'),
    new Cat('500', 500, 'Internal Server Error', './images/cat500.jpg'),
    new Cat('511', 500, 'Network Authentication Required', './images/cat511.jpg')
];

export {
    cats
};