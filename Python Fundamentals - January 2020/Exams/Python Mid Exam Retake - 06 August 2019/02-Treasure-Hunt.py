initial_loot = input().split('|')
d = 0

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Yohoho!':
        if initial_loot:
            for i in range(len(initial_loot)):
                d += len(initial_loot[i])
            print(f'Average treasure gain: {d / len(initial_loot):.2f} pirate credits.')
        elif not initial_loot:
            print(f'Failed treasure hunt.')
        exit()
    if command == 'Loot':
        for i in range(1, len(cmd)):
            if cmd[i] not in initial_loot:
                initial_loot.insert(0, cmd[i])
    elif command == 'Drop':
        index = int(cmd[1])
        skarida = ''
        if index <= len(initial_loot) - 1 and index >= 0:
            skarida = initial_loot[index]
            initial_loot.pop(index)
            initial_loot.append(skarida)
    elif command == 'Steal':
        count = int(cmd[1])
        if count > len(initial_loot) - 1:
            print(*initial_loot, sep=', ')
            initial_loot.clear()
        else:
            appender = []
            for i in range(-1, -count - 1, -1):
                appender.append(initial_loot[i])
            appender.reverse()
            print(*appender, sep=', ')
            for i in range(-1, -count - 1, -1):
                initial_loot.pop(-1)