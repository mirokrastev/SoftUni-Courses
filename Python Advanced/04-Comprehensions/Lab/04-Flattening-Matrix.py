matrix = []
d = int(input())
for i in range(d):
    for l in list(map(int, input().split(', '))):
        matrix.append(l)
print(matrix)