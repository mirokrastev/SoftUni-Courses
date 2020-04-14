import sys
high_num = -sys.maxsize
low_num = sys.maxsize
n = int(input())

for i in range(0, n):
    num = int(input())
    if num < low_num:
        low_num = num
    if num > high_num:
        high_num = num
print(f'Max number: {high_num}')
print(f'Min number: {low_num}')