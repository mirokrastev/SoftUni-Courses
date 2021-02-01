function solve(jsonInput, predicate) {
    let [key, value] = predicate.split('-');
    let cc = 0;
    return JSON.parse(jsonInput)
        .filter(entry => {
            if (key === 'all') return true;
            return entry[key] === value;
        }).map(entry => {
            cc++;
            return `${cc-1}. ${entry.first_name} ${entry.last_name} - ${entry.email}`
        }).join('\n');
}