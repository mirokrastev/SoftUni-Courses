function solve() {
    let cart = {};
    let resultEl = document.querySelector('.shopping-cart > textarea:nth-child(5)');

    let addButtons = Array.from(document.querySelectorAll('button.add-product'));
    addButtons.forEach(btn => btn.addEventListener('click', addToCart));

    let checkoutButton = document.querySelector('.checkout');
    checkoutButton.addEventListener('click', checkOut);

    function addToCart(event) {
        let element = event.target.parentElement.parentElement;
        let productName = element.querySelector('div.product-title').textContent;
        let productPrice = element.querySelector('div.product-line-price').childNodes[0].textContent;
        if (!cart.hasOwnProperty(productName)) {
            cart[productName] = {'price': 0}
        }
        cart[productName]['price'] += Number(productPrice);
        resultEl.textContent += `Added ${productName} for ${productPrice} to the cart.\n`
    }

    function checkOut() {
        addButtons.forEach(btn => btn.disabled = true);
        checkoutButton.disabled = true;
        let totalPrice = Object.values(cart).reduce((a, c) => a+c.price, 0);
        resultEl.textContent += `You bought ${Object.keys(cart).join(', ')} for ${totalPrice.toFixed(2)}.`
    }
}