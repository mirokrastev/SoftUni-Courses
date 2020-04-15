inp = input().split()
d = {}

for i in range(0, len(inp), 2):
    key = inp[i]
    value = inp[i+1]
    d[key] = int(value)
print(d)