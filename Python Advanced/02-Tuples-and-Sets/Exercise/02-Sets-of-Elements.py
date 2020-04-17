n, m = [int(i) for i in input().split()]
set_one = set(int(input()) for i in range(n))
set_two = set(int(input()) for i in range(m))
[print(i) for i in set_one.intersection(set_two)]