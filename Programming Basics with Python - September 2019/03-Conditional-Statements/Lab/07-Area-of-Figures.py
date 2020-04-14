import math

a = input()

if a == 'square':
    a = float(input())
    print(f'{a*a:.3f}')
elif a == 'rectangle':
    a = float(input())
    b = float(input())
    print(f'{a*b:.3f}')
elif a == 'circle':
    a = float(input())
    print(f'{math.pi * a * a:.3f}')
else:
    a = float(input())
    h = float(input())
    print(f'{(a*h)/2:.3f}')