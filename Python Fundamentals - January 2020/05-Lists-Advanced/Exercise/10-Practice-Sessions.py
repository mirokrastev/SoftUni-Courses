d = {}

while True:
    cmd = input().split('->')
    command = cmd[0]
    if command == 'END':
        sorted_d = sorted(d.items(), key=lambda x: (-len(x[1]), x[0]))
        print('Practice sessions:')
        for i in sorted_d:
            print(f'{i[0]}')
            for l in i[1]:
                print(f'++{l}')
        exit()
    if command == 'Add':
        road = cmd[1]
        racer = cmd[2]
        if road not in d:
            d[road] = []
            d[road].append(racer)
            continue
        elif road in d:
            d[road].append(racer)
    elif command == 'Move':
        currentroad = cmd[1]
        racer = cmd[2]
        nextroad = cmd[3]
        if racer in d[currentroad]:
            d[nextroad].append(racer)
            d[currentroad].remove(racer)
    elif command == 'Close':
        road = cmd[1]
        if road in d:
            d.pop(road)