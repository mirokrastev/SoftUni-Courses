vip_guests = []
regular_guests = []


def fn(a):
    if a[0].isnumeric():
        vip_guests.append(a)
    else:
        regular_guests.append(a)

def print_exit(a, b):
    print(f'{len(a) + len(b)}')
    for i in sorted(a):
        print(i)
    for i in sorted(b):
        print(i)
    exit()

def remove(a):
    if a[0].isnumeric():
        if a in vip_guests:
            vip_guests.remove(a)
    else:
        if a in regular_guests:
            regular_guests.remove(a)

def until_end():
    while True:
        inp = input()
        if inp == 'END':
            print_exit(vip_guests, regular_guests)
        else:
            remove(inp)


while True:
    inp = input()
    if inp == 'PARTY':
        until_end()
    fn(inp)