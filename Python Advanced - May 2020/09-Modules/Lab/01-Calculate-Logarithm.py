from math import log


def calculate_log(num, base):
    if base.isnumeric():
        return f'{log(num, int(base)):.2f}'
    return f'{log(num):.2f}'


num = int(input())
base = input()
print(calculate_log(num, base))