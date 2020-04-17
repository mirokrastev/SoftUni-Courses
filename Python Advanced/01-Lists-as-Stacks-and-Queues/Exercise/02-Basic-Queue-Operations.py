from collections import deque


def fn(a, b):
    que = deque(i for i in b)
    [que.popleft() for _ in range(a[1])]
    num_to_check = a[2]

    if num_to_check in que:
        return True
    elif not que:
        return 0
    else:
        return min(que)


first_inp = list(map(lambda x: int(x), input().split()))
second_inp = list(map(lambda x: int(x), input().split()))
print(fn(first_inp, second_inp))