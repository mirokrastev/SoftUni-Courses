x = int(input())
p1 = 0
p2 = 0
p3 = 0

for i in range(x):
    num = int(input())

    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1


p1 = p1 / x * 100
p2 = p2 / x * 100
p3 = p3 / x * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')