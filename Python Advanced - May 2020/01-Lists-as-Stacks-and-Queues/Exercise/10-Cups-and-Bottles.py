from collections import deque


def fill_water(bottle):
    global wasted_water

    cups[0] -= bottle
    if cups[0] <= 0:
        wasted_water += abs(cups[0])
        cups.popleft()


cups = deque(int(i) for i in input().split())
bottles = [int(i) for i in input().split()]
wasted_water = 0

while True:
    if not cups:
        print(f'Bottles: {" ".join(map(str, bottles[::-1]))}')
        break
    elif not bottles:
        print(f'Cups: {" ".join(map(str, cups))}')
        break
    bottle = bottles.pop()
    fill_water(bottle)

print(f'Wasted litters of water: {wasted_water}')