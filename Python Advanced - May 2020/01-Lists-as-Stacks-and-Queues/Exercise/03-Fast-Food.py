from _collections import deque

initial_food = int(input())
s = deque(int(i) for i in input().split())
biggest_order = max(s)
print(biggest_order)

while s:
    current_order = s.popleft()
    if current_order <= initial_food:
        initial_food -= current_order
    else:
        s.appendleft(current_order)
        print(f'Orders left: {" ".join(map(str, s))}')
        exit()

print('Orders complete')