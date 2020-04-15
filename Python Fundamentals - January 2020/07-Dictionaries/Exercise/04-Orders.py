d = {}
printer = {}

while True:
    cmd = input().split()
    if cmd[0] == 'buy':
        for i in d:
            printer[i] = d[i][0] * d[i][1]
        for i in printer:
            print(f'{i} -> {printer[i]:.2f}')
        exit()
    name = cmd[0]
    price = float(cmd[1])
    quantity = float(cmd[2])
    if name not in d:
        d[name] = [price, quantity]
    elif name in d:
        d[name][0] = price
        d[name][1] += quantity