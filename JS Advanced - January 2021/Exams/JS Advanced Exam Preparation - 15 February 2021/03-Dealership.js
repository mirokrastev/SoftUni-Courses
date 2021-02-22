describe('TestZadacha', () => {
    it('FirstTest', () => {
        assert.equal(dealership.newCarCost('BMW M4', 250000), 250000);
        assert.equal(dealership.newCarCost('Audi A4 B8', 25000), 10000);
        assert.equal(dealership.newCarCost('Audi A6 4K', 15000), -5000);
        assert.equal(dealership.newCarCost('Audi A8 D5', 30000), 5000);
        assert.equal(dealership.newCarCost('Audi TT 8J', 14000), 0);
        assert.equal(dealership.newCarCost('Audi TT 7J', 26000), 26000);
    });
    it('SecondTest', () => {
        assert.deepEqual(dealership.carEquipment(
            ['heated seats', 'sliding roof', 'sport rims', 'navigation']
        , [0, 3]), ['heated seats', 'navigation']);
        assert.deepEqual(dealership.carEquipment(
            ['heated seats']
            , [0, 1]), ['heated seats', undefined]);
        assert.deepEqual(dealership.carEquipment(
            ['heated seats', 'roof', 'side']
            , [0, 1, 2]), ['heated seats', 'roof', 'side']);
        assert.deepEqual(dealership.carEquipment(
            ['heated seats', 'roof', 'side']
            , [0, 1, 2, 5]), ['heated seats', 'roof', 'side', undefined]);
    });
    it('ThirdTest', () => {
        assert.equal(dealership.euroCategory(3), 'Your euro category is low, so there is no discount from the final price!');
        assert.equal(dealership.euroCategory(4), `We have added 5% discount to the final price: 14250.`);
        assert.equal(dealership.euroCategory(6), `We have added 5% discount to the final price: 14250.`);
    })
})