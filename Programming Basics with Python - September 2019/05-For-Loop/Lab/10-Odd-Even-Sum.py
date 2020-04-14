n = int(input())
evenSum = 0
oddSum = 0

for i in range(1, n+1):
    num = int(input())
    if i % 2 == 0:
        evenSum += num
    elif i % 2 != 0:
        oddSum += num
diff = oddSum - evenSum
if evenSum == oddSum:
    print(f'Yes\nSum = {evenSum}')
else:
    if diff < 0:
        diff = evenSum - oddSum
        print(f'No\nDiff = {diff}')
        exit()
    print(f'No\nDiff = {diff}')