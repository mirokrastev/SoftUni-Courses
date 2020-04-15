inp = input()

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Sign':
        exit()
    if command == 'Case':
        second_command = cmd[1]
        if second_command == 'lower':
            inp = inp.lower()
            print(inp)
        elif second_command == 'upper':
            inp = inp.upper()
            print(inp)
    elif command == 'Reverse':
        start_index = int(cmd[1])
        end_index = int(cmd[2])
        if 0 <= start_index <= end_index:
            if end_index <= len(inp) - 1:
                reversed_string = "".join(reversed(inp[start_index:end_index + 1]))
                print(reversed_string)
    elif command == 'Cut':
        substring = cmd[1]
        if substring in inp:
            inp = inp.replace(substring, '')
            print(inp)
        else:
            print(f'The word {inp} doesn\'t contain {substring}.')
    elif command == 'Replace':
        char = cmd[1]
        inp = inp.replace(char, '*')
        print(inp)
    elif command == 'Check':
        char = cmd[1]
        if char in inp:
            print('Valid')
        else:
            print(f'Your username must contain {char}.')