function solve(string) {
    let separators = [', ', ' ', '\\+', '-', ':', '\\.' , '\\?',
                      '\\*', '\\', '/', '!', '@', '#', '$', '%',
                      '\\^', '&', '\\(', '\\)', '=', '\\|', '`', 
                      '~', ';', '\'', '"', '[', ']', '{', '}']
    let finalArr = [];
    string.split(new RegExp(separators.join('|'), 'g'))
        .forEach((txt) => {
            if (txt === '') return;
            finalArr.push(txt.toUpperCase());
        });
    console.log(finalArr.join(', '));
}