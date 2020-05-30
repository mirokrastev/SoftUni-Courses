l = [i for i in input().split() if len(i) % 2 == 0]
[print(*i, sep='') for i in l]