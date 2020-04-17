def fn(a, b):
    s = [i for i in b]
    [s.pop() for _ in range(a[1])]
    num_to_check = a[2]
    if num_to_check in s:
        return True
    elif not s:
        return 0
    else:
        return min(s)


first_inp = list(map(lambda x: int(x), input().split()))
second_inp = list(map(lambda x: int(x), input().split()))
print(fn(first_inp, second_inp))