d = {}
while True:
    cmd = input().split(': ')
    if cmd[0] == 'statistics':
        print('Products in stock:')
        for i in d:
            print(f'- {i}: {d[i]}')
        print(f'Total Products: {len(d)}')
        print(f'Total Quantity: {sum(d.values())}')
        exit()
    key = cmd[0]
    value = int(cmd[1])
    if key not in d:
        d[key] = value
    else:
        d[key] += value