def absolute(inp):
    return list(filter(lambda x: x % 2 == 0, inp))


inp = [int(i) for i in input().split()]
print(absolute(inp))