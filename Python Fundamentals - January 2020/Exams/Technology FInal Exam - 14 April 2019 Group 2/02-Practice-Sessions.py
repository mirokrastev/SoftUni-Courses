d = {}

while True:
    cmd = input().split('->')
    command = cmd[0]
    if command == 'END':
        break
    if command == 'Add':
        road = cmd[1]
        racer = cmd[2]
        if road not in d:
            d[road] = []
        d[road].append(racer)
    elif command == 'Move':
        current_road = cmd[1]
        racer = cmd[2]
        next_road = cmd[3]
        if racer in d[current_road]:
            d[current_road].remove(racer)
            d[next_road].append(racer)
    elif command == 'Close':
        road = cmd[1]
        if road in d:
            d.pop(road)

sorted_d = dict(sorted(d.items(), key=lambda x: (-len(x[1]), x[0])))
print('Practice sessions:')
for k,v in sorted_d.items():
    print(f'{k}')
    for l in v:
        print(f'++{l}')