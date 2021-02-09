function solve(array, startIndex, endIndex) {
    if (!Array.isArray(array)) return NaN;
    startIndex = startIndex > 0 ? startIndex > array.length ? 0 : startIndex : 0;
    endIndex = endIndex > array.length-1 ? array.length : endIndex;
    return array.slice(startIndex, endIndex+1).map(Number).reduce((a, c) => a+c, 0);
}