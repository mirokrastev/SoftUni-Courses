def occurrences(num):
    if num not in d:
        d[num] = 0
    d[num] += 1


nums = [float(i) for i in input().split()]
d = {}
[occurrences(i) for i in nums]

for k, v in d.items():
    print(f'{k} - {v} times')