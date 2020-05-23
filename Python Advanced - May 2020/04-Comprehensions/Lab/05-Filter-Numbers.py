def fn(num):
    result = [x for x in range(2, 10) if num % x == 0]
    return True if result else False

print([i for i in range(int(input()), int(input()) + 1) if fn(i)])