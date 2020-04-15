string = input()

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Done':
        exit()
    if command == 'Change':
        char = cmd[1]
        replacement = cmd[2]
        string = string.replace(char, replacement)
        print(string)
    elif command == 'Includes':
        string_var = cmd[1]
        if string_var in string:
            print('True')
        else:
            print('False')
    elif command == 'End':
        string_var = cmd[1]
        print(string.endswith(string_var))
    elif command == 'Uppercase':
        string = string.upper()
        print(string)
    elif command == 'FindIndex':
        char = cmd[1]
        if char in string:
            print(string.index(char))
    elif command == 'Cut':
        start_index = int(cmd[1])
        length = int(cmd[2])
        string = string[start_index:(start_index + length)]
        print(string)