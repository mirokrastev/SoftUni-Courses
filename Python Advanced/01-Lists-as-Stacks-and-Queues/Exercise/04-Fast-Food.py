from collections import deque


def fn(quantity_food, quantity_order):
    while True:
        if not quantity_order:
            return f'Orders complete'
        if quantity_order:
            if quantity_food >= quantity_order[0]:
                quantity_food -= quantity_order.popleft()
            else:
                return f'Orders left: {" ".join([str(i) for i in quantity_order])}'

quantity_food = int(input())
quantity_order = deque(map(int, input().split()))
print(max(quantity_order))
print(fn(quantity_food, quantity_order))