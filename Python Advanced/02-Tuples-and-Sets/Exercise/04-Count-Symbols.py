d = {}

def fn(a):
    if a not in d:
        d[a] = 0
    d[a] += 1

inp = input()
[fn(i) for i in inp]
for k,v in sorted(d.items()):
    print(f'{k}: {v} time/s')