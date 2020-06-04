def odd_or_even(num):
    if num % 2 == 0:
        d['Even'] += num
    else:
        d['Odd'] += num


command = input()
arg = [int(i) for i in input().split()]
d = {'Odd': 0, 'Even': 0}
[odd_or_even(i) for i in arg]

print(d[command] * len(arg))