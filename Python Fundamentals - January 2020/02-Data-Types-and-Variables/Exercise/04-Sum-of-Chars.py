n = int(input())
b = 0
for i in range(n):
    char = input()
    b += ord(char)
print(f'The sum equals: {b}')