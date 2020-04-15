inp = int(input())
d = []
counter = 1

while True:
    if inp == 0:
        print(d)
        break
    if 2*counter**2 <= inp:
        d.append(2*counter**2)
        inp -= 2*counter**2
    elif inp < 2*counter**2:
        d.append(inp)
        inp -= inp
    counter += 1