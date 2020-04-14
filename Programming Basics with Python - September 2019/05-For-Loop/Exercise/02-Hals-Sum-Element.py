num = int(input())
max_num = -10000000000
sum = 0

for i in range(num):
    n = int(input())
    sum += n

    if max_num < n:
        max_num = n

sum -= max_num
if sum == max_num:
    print(f'Yes\nSum = {sum}')
else:
    diff = abs(sum-max_num)
    print(f'No\nDiff = {diff}')