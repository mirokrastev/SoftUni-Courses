num = int(input())


def rhombus(num):
    for i in range(1, num + 1):
        print(' ' * (num - i) + '* ' * i)
    for i in range(1, num):
        print(' ' * i + '* ' * (num - i))


rhombus(num)