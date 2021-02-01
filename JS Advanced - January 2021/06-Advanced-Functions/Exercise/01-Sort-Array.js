function solve(array, criteria) {
    return array.sort((a, b) => criteria === 'asc' ? a - b : b - a);
}