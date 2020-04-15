d = {}

while True:
    cmd = input().split('->')
    command = cmd[0]
    if command == 'END':
        break
    if 'Add' in cmd:
        store = cmd[1]
        if store not in d:
            d[store] = []
        var = str(cmd[2]).split(',')
        for i in var:
            d[store].append(i)
    elif command == 'Remove':
        store = cmd[1]
        if store in d:
            d.pop(store)

sorted_d = dict(sorted(d.items(), key=lambda x: (len(x[1]), x[0]), reverse=True))
print('Stores list:')
for k,v in sorted_d.items():
    print(k)
    for l in v:
        print(f'<<{l}>>')