factor = int(input())
count = int(input())
d = []

for i in range(factor, factor * count + 1, factor):
    d.append(i)
print(d)