function solve(numOne, numTwo, op) {
    let dd = {'+': numOne + numTwo, '-': numOne - numTwo,
              '*': numOne * numTwo, '/': numOne / numTwo,
              '%': numOne % numTwo, '**': numOne ** numTwo};
    console.log(dd[op]);
}