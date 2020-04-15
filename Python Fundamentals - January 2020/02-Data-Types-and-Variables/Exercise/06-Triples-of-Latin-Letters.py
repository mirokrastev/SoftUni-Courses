n = int(input())

for i in range(n):
    for l in range(n):
        for b in range(n):
            print(f'{chr(97+i)}{chr(97+l)}{chr(97+b)}')