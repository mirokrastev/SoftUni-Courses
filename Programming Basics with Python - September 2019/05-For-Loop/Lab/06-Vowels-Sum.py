str = input().lower()
sum = 0

for c in str:
    if c == 'a':
        sum += 1
    elif c == 'e':
        sum += 2
    elif c == 'i':
        sum += 3
    elif c == 'o':
        sum += 4
    elif c == 'u':
        sum += 5
print(sum)