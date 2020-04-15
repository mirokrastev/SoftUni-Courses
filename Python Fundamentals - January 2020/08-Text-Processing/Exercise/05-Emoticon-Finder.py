inp = input()
d = []

for i in range(len(inp)):
    if inp[i] == ':':
        d.append(':' + inp[i+1])
print(*d, sep='\n')