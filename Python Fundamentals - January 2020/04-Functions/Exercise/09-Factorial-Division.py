num_one = int(input())
num_two = int(input())


def fn(a,b):
    d = a
    h = b
    for i in range(a - 1, 0, -1):
        d *= i
    for l in range(b - 1, 0, -1):
        h *= l
    return f'{d / h:.2f}'



print(fn(num_one, num_two))