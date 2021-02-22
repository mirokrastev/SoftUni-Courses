describe('Tests', () => {
    it('makeAnOrderTests', () => {
        assert.throw(() => pizzUni.makeAnOrder({'name': 'margarita'}), Error, /You must order at least 1 Pizza to finish the order./);

        assert.equal(pizzUni.makeAnOrder({'orderedPizza': 'a'}), 'You just ordered a');
        assert.equal(pizzUni.makeAnOrder({'orderedPizza': 'a', 'orderedDrink': 'b'}), 'You just ordered a and b.');

        assert.throw(() => pizzUni.makeAnOrder({'a': 'a', 'orderedDrink': 'b'}), Error, /You must order at least 1 Pizza to finish the order./);
    });
    it('getRemainingWorkTests', () => {
        assert.equal(pizzUni.getRemainingWork([{pizzaName: 'a', 'status': 'preparing'}]), 'The following pizzas are still preparing: a.')
        assert.equal(pizzUni.getRemainingWork([{pizzaName: 'b', 'status': 'ready'}]), 'All orders are complete!');
        assert.equal(pizzUni.getRemainingWork([{pizzaName: 'c', 'status': 'ready'}, {pizzaName: 'd', 'status': 'preparing'}]),
            'The following pizzas are still preparing: d.');
        assert.equal(pizzUni.getRemainingWork([{pizzaName: 'e', 'status': 'preparing'}, {pizzaName: 'f', 'status': 'preparing'}]),
            'The following pizzas are still preparing: e, f.');
        assert.equal(pizzUni.getRemainingWork([{pizzaName: 'q', 'status': 'ready'}, {pizzaName: 'w', 'status': 'ready'}]),
            'All orders are complete!');
    });
    it('orderTypeTests', () => {
        assert.equal(pizzUni.orderType(500, 'Delivery'), 500);
        assert.equal(pizzUni.orderType(500, 'Carry Out'), 450);
    })
})