a = int(input())
counter = 0
empty = []

for i in range(a):
    counter += 1
    empty.append(f'{counter} sheep...')

print("".join(empty))