from collections import deque
s = deque()


def fn(n):
    op = n[0]
    if op == 1:
        s.append(n[1])
    if s:
        if op == 2:
            if s:
                s.pop()
        elif op == 3:
            if s:
                print(max(s))
        elif op == 4:
            if s:
                print(min(s))


num = int(input())
for i in range(num):
    inp = list(map(lambda x: int(x), input().split()))
    fn(inp)

print(*reversed(s), sep=', ')