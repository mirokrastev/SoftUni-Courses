d = set()

def fn(a):
    command = a[0]
    if command == 'END':
        if d:
            [print(i) for i in d]
        else:
            print('Parking Lot is Empty')
        exit()
    number = a[1]
    if command == 'IN':
        d.add(number)
    elif command == 'OUT':
        if number in d:
            d.remove(number)


while True:
    inp = input().split(', ')
    fn(inp)