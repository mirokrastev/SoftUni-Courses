from collections import deque

cups_queue = deque(int(i) for i in input().split())
bottles_stack = deque(int(i) for i in input().split())
wasted_water = 0

while True:
    if not cups_queue:
        print(f'Bottles: {" ".join([str(i) for i in bottles_stack])}')
        print(f'Wasted litters of water: {wasted_water}')
        exit()
    if not bottles_stack:
        print(f'Cups: {" ".join([str(i) for i in cups_queue])}')
        print(f'Wasted litters of water: {wasted_water}')
        exit()
    first_cup = cups_queue[0]
    while True:
        water = bottles_stack.pop()
        first_cup -= water
        if first_cup <= 0:
            cups_queue.popleft()
            wasted_water += abs(first_cup)
            break