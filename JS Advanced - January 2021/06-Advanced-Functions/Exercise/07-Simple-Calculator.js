function solve() {
    return {
        init(selectorOne, selectorTwo, resultSelector) {
            this.selectorOne = document.querySelector(selectorOne);
            this.selectorTwo = document.querySelector(selectorTwo);
            this.resultSelector = document.querySelector(resultSelector);
        },

        add() {
            this.resultSelector.value = Number(this.selectorOne.value) + Number(this.selectorTwo.value);
        },

        subtract() {
            this.resultSelector.value = Number(this.selectorOne.value) - Number(this.selectorTwo.value);
        }
    }
}