from collections import deque

def add_people(arg):
    que.append(arg)

def until_end():
    global quantity
    while True:
        arg = input().split()
        if arg[0] == 'End':
            return f'{quantity} liters left'
        elif arg[0] == 'refill':
            quantity += int(arg[1])
        else:
            if int(arg[0]) <= quantity:
                print(f'{que.popleft()} got water')
                quantity -= int(arg[0])
            else:
                print(f'{que.popleft()} must wait')

quantity = int(input())
que = deque()

while True:
    arg = input()
    if arg != 'Start':
        add_people(arg)
    else:
        print(until_end())
        break