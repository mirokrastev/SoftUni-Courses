inp = input()

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Finish':
        exit()
    if command == 'Replace':
        current_char = cmd[1]
        new_char = cmd[2]
        inp = inp.replace(current_char, new_char)
        print(inp)
    elif command == 'Cut':
        start_index = int(cmd[1])
        end_index = int(cmd[2])
        if 0 <= start_index <= end_index:
            if end_index <= len(inp) - 1:
                inp = inp[:start_index] + inp[end_index + 1:]
                print(inp)
            else:
                print('Invalid indexes!')
        else:
            print('Invalid indexes!')
    elif command == 'Make':
        second_command = cmd[1]
        if second_command == 'Upper':
            inp = inp.upper()
            print(inp)
        elif second_command == 'Lower':
            inp = inp.lower()
            print(inp)
    elif command == 'Check':
        string = cmd[1]
        if string in inp:
            print(f'Message contains {string}')
        else:
            print(f'Message doesn\'t contain {string}')
    elif command == 'Sum':
        start_index = int(cmd[1])
        end_index = int(cmd[2])
        if 0 <= start_index <= end_index:
            if end_index <= len(inp) - 1:
                d = []
                for i in inp[start_index:end_index + 1]:
                    num = ord(i)
                    d.append(num)
                print(sum(d))
            else:
                print('Invalid indexes!')
        else:
            print('Invalid indexes!')