num = int(input())
s = set()

for i in range(num):
    inp = input().split()
    for l in inp:
        s.add(l)

[print(i) for i in s]