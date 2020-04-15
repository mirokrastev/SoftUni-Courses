string = input()

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'For' and cmd[1] == 'Azeroth':
        exit()
    if command == 'GladiatorStance':
        string = string.upper()
        print(string)
    elif command == 'DefensiveStance':
        string = string.lower()
        print(string)
    elif command == 'Dispel':
        index = int(cmd[1])
        letter = cmd[2]
        if len(string) - 1 >= index >= 0:
            string = string[:index] + letter + string[index+1:]
            print('Success!')
        else:
            print('Dispel too weak.')
    elif command == 'Target':
        second_command = cmd[1]
        if second_command == 'Change':
            substring = cmd[2]
            second_substring = cmd[3]
            string = string.replace(substring, second_substring)
            print(string)
        elif second_command == 'Remove':
            substring = cmd[2]
            string = string.replace(substring, '')
            print(string)
        else:
            print('Command doesn\'t exist!')
    else:
        print('Command doesn\'t exist!')