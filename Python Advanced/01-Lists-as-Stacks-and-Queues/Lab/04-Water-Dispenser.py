from _collections import deque
global dispenser
dispenser = int(input())
que = deque()

def water_dispenser(a):
    global dispenser
    if a == 'End':
        print(f'{dispenser} liters left')
        exit()

    if a == 'Start':
        return

    if a.isnumeric():
        check = int(a)
        if check <= dispenser:
            print(f'{que.popleft()} got water')
            dispenser -= check
        else:
            print(f'{que.popleft()} must wait')
    elif 'refill' in a:
        splitted = a.split()
        to_refill = int(splitted[1])
        dispenser += to_refill
    else:
        que.append(a)


while True:
    water_dispenser(input())