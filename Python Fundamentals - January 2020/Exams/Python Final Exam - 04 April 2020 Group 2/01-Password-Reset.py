string = input()

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Done':
        print(f'Your password is: {string}')
        exit()
    if command == 'TakeOdd':
        raw_pass = ''
        for i in range(1, len(string)):
            if i % 2 == 1:
                raw_pass += string[i]
        string = raw_pass
        print(string)
    elif command == 'Cut':
        index = int(cmd[1])
        length = int(cmd[2])
        string = string[:index] + string[index+length:]
        print(string)
    elif command == 'Substitute':
        substring = cmd[1]
        substitute = cmd[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print('Nothing to replace!')