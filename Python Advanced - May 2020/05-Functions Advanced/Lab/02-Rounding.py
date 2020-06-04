def rounding(inp):
    return list(map(round, inp))


inp = [float(i) for i in input().split()]
print(rounding(inp))