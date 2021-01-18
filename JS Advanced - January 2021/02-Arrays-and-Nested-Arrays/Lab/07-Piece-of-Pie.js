function solve(array, startSection, endSection) {
    return array.slice(array.indexOf(startSection), array.indexOf(endSection)+1);
}