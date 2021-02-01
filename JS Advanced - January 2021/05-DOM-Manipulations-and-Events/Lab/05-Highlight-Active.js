function focus() {
    let mainDiv = document.getElementsByTagName('div')[0]
    let allDivs = mainDiv.getElementsByTagName('div');

    console.log(allDivs);
    for (let iterator of allDivs) {
        iterator.children[1].addEventListener('focus',
            function(event) {
            event.target.parentElement.setAttribute('class', 'focused');
        })
        iterator.children[1].addEventListener('blur',
            function(event) {
            event.target.parentElement.removeAttribute('class');
        })
    }
}