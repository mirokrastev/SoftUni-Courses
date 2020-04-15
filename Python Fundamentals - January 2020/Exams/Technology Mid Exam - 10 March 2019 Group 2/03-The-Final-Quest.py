inp = input().split()

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Stop':
        print(*inp, sep=' ')
        exit()
    if command == 'Delete':
        index = int(cmd[1]) + 1
        if index <= len(inp) - 1 and index >= 1:
            inp.pop(index)
    elif command == 'Swap':
        word_one = cmd[1]
        word_two = cmd[2]
        if all([word_one in inp, word_two in inp]):
            index_one = inp.index(word_one)
            index_two = inp.index(word_two)
            inp[index_one], inp[index_two] = \
                inp[index_two], inp[index_one]
    elif command == 'Put':
        word = cmd[1]
        index = int(cmd[2]) - 1
        if index <= len(inp) and index >= 0:
            inp.insert(index, word)
    elif command == 'Sort':
        inp.sort(reverse=True)
    elif command == 'Replace':
        word_one = cmd[1]
        word_two = cmd[2]
        if word_two in inp:
            index = inp.index(word_two)
            inp[index] = word_one