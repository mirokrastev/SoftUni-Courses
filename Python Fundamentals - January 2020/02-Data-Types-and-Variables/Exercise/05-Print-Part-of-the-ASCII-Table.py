a = int(input())
b = int(input())
d = []

for i in range(a,b + 1):
    d.append(chr(i))
print(*d, sep=' ')