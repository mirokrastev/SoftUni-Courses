alphabet = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}
d = 0
inp = input().split()
for i in range(len(inp)):
    if inp[i][0] in alphabet:
        num = int(inp[i][1:-1])
        d += num * alphabet[inp[i][0]]
    elif inp[i][0].lower() in alphabet:
        num = int(inp[i][1:-1])
        d += num / alphabet[inp[i][0].lower()]
    if inp[i][-1] in alphabet:
        d += alphabet[inp[i][-1]]
    elif inp[i][-1].lower() in alphabet:
        d -= alphabet[inp[i][-1].lower()]
print(f'{d:.2f}')