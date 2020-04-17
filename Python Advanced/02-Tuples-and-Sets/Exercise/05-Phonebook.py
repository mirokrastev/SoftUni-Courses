d = {}

def until_stop():
    while True:
        inp = input()
        if inp == 'stop':
            exit()
        if inp in d:
            print(f'{inp} -> {d[inp]}')
        else:
            print(f'Contact {inp} does not exist.')

def append(a):
    name, phone = a.split('-')
    if name not in d:
        d[name] = phone
    else:
        d[name] = phone

while True:
    inp = input()
    if inp == 'search':
        until_stop()
    else:
        append(inp)