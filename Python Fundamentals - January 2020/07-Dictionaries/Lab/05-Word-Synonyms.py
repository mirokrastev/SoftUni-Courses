inp = int(input())
d = {}

for i in range(inp):
    word = input()
    synonym = input()
    if word not in d:
        d[word] = []
    d[word].append(synonym)

for i in d:
    print(f"{i} - {', '.join(d[i])}")