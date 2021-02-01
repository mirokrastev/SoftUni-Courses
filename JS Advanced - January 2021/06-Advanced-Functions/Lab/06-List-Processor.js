function solve(input) {
    let outputArray = [];

    function listProcessorBuilder() {
        return (command, commandInput=undefined) => {
            let add = input => outputArray.push(input);
            let remove = input => outputArray = outputArray.filter((el) => el !== input);
            let print = () => console.log(outputArray.join(','));
            let mapper = {'add': add, 'remove': remove, 'print': print}[command](commandInput)
        }
    }

    let listProcessor = listProcessorBuilder();
    input.forEach(input => listProcessor(...input.split(' ')))
}