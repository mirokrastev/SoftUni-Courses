describe('Test is Odd or Even String', () => {
    it('should return undefined for nonstrings', () => {
        let actual = isOddOrEven(['string']);
        assert.isUndefined(actual);
    });
    it('should return even for string', () => {
        let actual = isOddOrEven('asdq');
        assert.equal(actual, 'even');
    });
    it('should return odd for string', () => {
        let actual = isOddOrEven('asd');
        assert.equal(actual, 'odd');
    });
    it('should pass random tests', () => {
        assert.equal(isOddOrEven('zdraveite'), 'odd');
        assert.equal(isOddOrEven('zdraveite!'), 'even');
    })
})