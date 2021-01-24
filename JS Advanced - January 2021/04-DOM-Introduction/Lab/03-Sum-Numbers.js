function calc() {
    let [numOne, numTwo] = [document.getElementById('num1'), document.getElementById('num2')];
    let resultEl = document.getElementById('sum');
    resultEl.value = Number(numOne.value) + Number(numTwo.value);
}