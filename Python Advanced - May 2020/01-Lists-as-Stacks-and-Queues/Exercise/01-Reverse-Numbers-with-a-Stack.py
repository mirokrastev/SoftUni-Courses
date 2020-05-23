initial_list = [int(i) for i in input().split()]
s = [i for i in initial_list[::-1]]
print(*s)