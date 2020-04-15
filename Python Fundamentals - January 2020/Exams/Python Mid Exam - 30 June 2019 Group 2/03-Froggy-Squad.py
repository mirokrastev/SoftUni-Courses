name_frogs = input().split()
appender = []

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Join':
        name = cmd[1]
        name_frogs.append(name)
    elif command == 'Jump':
        name = cmd[1]
        index = int(cmd[2])
        if index <= len(name_frogs) - 1 and index >= 0:
            name_frogs.insert(index, name)
    elif command == 'Dive':
        index = int(cmd[1])
        if index <= len(name_frogs) - 1 and index >= 0:
            name_frogs.pop(index)
    elif command == 'First':
        count = int(cmd[1])
        appender = []
        if count > len(name_frogs) - 1:
            print(*name_frogs, sep=' ')
        else:
            for i in range(count):
                appender.append(name_frogs[i])
            print(*appender, sep=' ')
    elif command == 'Last':
        count = int(cmd[1])
        appender = []
        if count > len(name_frogs) - 1:
            print(*name_frogs, sep=' ')
        else:
            for i in range(-1, -count - 1, -1):
                appender.append(name_frogs[i])
            appender.reverse()
            print(*appender, sep=' ')
    elif command == 'Print' and cmd[1] == 'Normal':
        print(f'Frogs: {" ".join(name_frogs)}')
        exit()
    elif command == 'Print' and cmd[1] == 'Reversed':
        name_frogs.reverse()
        print(f'Frogs: {" ".join(name_frogs)}')
        exit()