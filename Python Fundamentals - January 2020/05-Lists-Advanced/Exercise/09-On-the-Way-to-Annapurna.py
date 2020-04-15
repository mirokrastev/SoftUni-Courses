d = {}

while True:
    cmd = input().split('->')
    command = cmd[0]
    if command == 'END':
        print('Stores list:')
        sorted_d = sorted(d.items(), key=lambda x: (len(x[1]), x[0]), reverse=True)
        for i in sorted_d:
            print(f'{i[0]}')
            for l in i[1]:
                print(f'<<{l}>>')
        exit()
    if command == 'Add':
        store = cmd[1]
        if store not in d:
            d[store] = []
        inp = cmd[2].split(',')
        d[store].extend(i for i in inp)
    elif command == 'Remove':
        store = cmd[1]
        if store in d:
            d.pop(store)