describe('TestMathEnforcer', () => {
    it('should return undefined', () => {
        let addFiveMethod = mathEnforcer.addFive;
        assert.isUndefined(addFiveMethod('5'));
        assert.isUndefined(addFiveMethod([1]));
        assert.isUndefined(addFiveMethod('5.1'));

        let subtractTenMethod = mathEnforcer.subtractTen;
        assert.isUndefined(subtractTenMethod('5'));
        assert.isUndefined(subtractTenMethod([1]));
        assert.isUndefined(subtractTenMethod('5.1'));

        let sumMethod = mathEnforcer.sum;
        assert.isUndefined(sumMethod('1', '2'));
        assert.isUndefined(sumMethod(1, '2'));
        assert.isUndefined(sumMethod('1', 2));
        assert.isUndefined(sumMethod([1], '2'));
        assert.isUndefined(sumMethod(5, '5.2'));
        assert.isUndefined(sumMethod(6.2, 'asd'));
        assert.isUndefined(sumMethod('asd', 7645.123));
    });
    it('should return valid answer', () => {
        let addFiveMethod = mathEnforcer.addFive;
        assert.equal(addFiveMethod(5), 10);
        assert.equal(addFiveMethod(5.1), 10.1);
		assert.equal(addFiveMethod(-5), 0);
      
        let subtractTenMethod = mathEnforcer.subtractTen;
        assert.equal(subtractTenMethod(5), -5);
        assert.equal(subtractTenMethod(10), 0);
        assert.equal(subtractTenMethod(50), 40);
        assert.equal(subtractTenMethod(-10), -20);
        assert.equal(subtractTenMethod(50.20), 40.20);
        assert.equal(subtractTenMethod(-123.7), -133.7);

        let sumMethod = mathEnforcer.sum;
        assert.equal(sumMethod(5, 5), 10);
        assert.equal(sumMethod(5.1, 5), 10.1);
        assert.equal(sumMethod(-10, 5), -5);
        assert.equal(sumMethod(-1, -1), -2);
        assert.equal(sumMethod(-5.2, -1.7), -6.9);
        assert.equal(sumMethod(10, -5), 5);
        assert.equal(sumMethod(5.1, 2.2), 7.3);
        assert.closeTo(sumMethod(1.1 ,2.2), 3.3, 0.01);
        assert.closeTo(sumMethod(-1.1, -2.2), -3.3, 0.01);
    })
})