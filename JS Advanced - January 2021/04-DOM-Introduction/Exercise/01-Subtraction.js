function subtract() {
    let [numOne, numTwo] = [document.getElementById('firstNumber'), document.getElementById('secondNumber')];
    document.getElementById('result').innerText = Number(numOne.value) - Number(numTwo.value);
}