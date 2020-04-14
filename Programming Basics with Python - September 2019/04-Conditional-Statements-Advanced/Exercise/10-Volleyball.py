import math

year_type = input()
p = int(input())
h = int(input())

total_days = 0
total_days = (48 - h) * 3 / 4
total_days += h
total_days += p * 2 / 3

if year_type == 'leap':
    total_days *= 1.15
    print(math.floor(total_days))
elif year_type == 'normal':
    print(math.floor(total_days))