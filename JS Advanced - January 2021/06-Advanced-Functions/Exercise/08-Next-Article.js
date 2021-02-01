function getArticleGenerator(articles) {
    let index = 0;
    return () => {
        if (index > articles.length - 1) {
            return;
        }
        document.getElementById('content').innerHTML += `<article>${articles[index]}</article>`;
        index++
    }
}