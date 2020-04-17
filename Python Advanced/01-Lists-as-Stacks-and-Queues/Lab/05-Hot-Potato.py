from collections import deque

def hot_potato(children, toss):
    counter = 1
    while children:
        while counter != toss:
            removed = children.popleft()
            children.append(removed)
            counter += 1
        removed = children.popleft()
        if len(children) == 0:
            print(f'Last is {removed}')
        else:
            print(f'Removed {removed}')
        counter = 1

inp = deque(input().split())
toss = int(input())
hot_potato(inp, toss)