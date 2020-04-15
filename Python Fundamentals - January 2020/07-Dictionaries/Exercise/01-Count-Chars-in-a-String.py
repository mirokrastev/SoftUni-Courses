inp = input().replace(' ', '')
d = {}

for i in inp:
    if i not in d:
        d[i] = 0
    d[i] += 1

for i in d:
    print(f'{i} -> {d[i]}')