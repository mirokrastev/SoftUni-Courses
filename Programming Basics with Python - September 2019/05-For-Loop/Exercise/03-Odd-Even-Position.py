import sys
n = int(input())
sum_even = 0
sum_odd = 0
min_even = sys.maxsize
max_even = -sys.maxsize
min_odd = sys.maxsize
max_odd = -sys.maxsize

for i in range(n):
    i += 1
    num = float(input())
    if i % 2 == 0:
        sum_even += num
        if num > max_even:
            max_even = num
        if num < min_even:
            min_even = num
    elif i % 2 != 0:
        sum_odd += num
        if num > max_odd:
            max_odd = num
        if num < min_odd:
            min_odd = num
print(f'OddSum={sum_odd:.2f},')
if min_odd == sys.maxsize:
    min_odd = 'No'
    print(f'OddMin={min_odd},')
else:
    print(f'OddMin={min_odd:.2f},')
if max_odd == -sys.maxsize:
    max_odd = 'No'
    print(f'OddMax={max_odd},')
else:
    print(f'OddMax={max_odd:.2f},')
print(f'EvenSum={sum_even:.2f},')
if min_even == sys.maxsize:
    min_even = 'No'
    print(f'EvenMin={min_even},')
else:
    print(f'EvenMin={min_even:.2f},')
if max_even == -sys.maxsize:
    max_even = 'No'
    print(f'EvenMax={max_even}')
else:
    print(f'EvenMax={max_even:.2f}')