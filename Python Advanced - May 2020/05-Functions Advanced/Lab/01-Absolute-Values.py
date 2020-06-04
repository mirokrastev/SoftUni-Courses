def absolute(inp):
    return list(map(abs, inp))


inp = [float(i) for i in input().split()]
print(absolute(inp))