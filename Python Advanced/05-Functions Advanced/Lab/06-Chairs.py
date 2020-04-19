def combinations(values, k, comb=[]):
    if len(comb) == k:
        print(*comb, sep=', ')
        return
    for i in range(len(values)):
        x = values[i]
        comb.append(x)
        combinations(values[i + 1:], k, comb)
        comb.pop()

arg = input().split(', ')
chairs = int(input())
combinations(arg, chairs)