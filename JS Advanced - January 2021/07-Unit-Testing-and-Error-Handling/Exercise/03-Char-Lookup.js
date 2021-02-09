describe('TestCharLookup', () => {
    it('should return undefined', () => {
        assert.isUndefined(lookupChar(['string'], 1));
        assert.isUndefined(lookupChar('string', '1'));
        assert.isUndefined(lookupChar({0: 'string'}, '5'));
        assert.isUndefined(lookupChar({1: 'string'}, 'string'));
        assert.isUndefined(lookupChar('string', 1.5));
    });
    it('should return incorrect index', () => {
        assert.equal(lookupChar('string', 20), 'Incorrect index');
        assert.equal(lookupChar('string', 6), 'Incorrect index');
        assert.equal(lookupChar('string', -1), 'Incorrect index');
        assert.equal(lookupChar('string', -15), 'Incorrect index');
        assert.equal(lookupChar('', 5), 'Incorrect index');
        assert.equal(lookupChar('', 0), 'Incorrect index');
    });
    it('should return correct answer', () => {
        assert.equal(lookupChar('string', 0), 's');
        assert.equal(lookupChar('string', 3), 'i');
        assert.equal(lookupChar('string', 5), 'g');
        assert.equal(lookupChar('string', 1), 't');
        assert.equal(lookupChar('test', 3), 't');
    })
})