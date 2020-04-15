text = input()
for_print = ""
boom = 0

for x in range(len(text)):
    if text[x] == ">":
        for_print += text[x]
        boom += int(text[x + 1])
        continue
    if boom:
        boom -= 1
        continue
    for_print += text[x]

print(for_print)