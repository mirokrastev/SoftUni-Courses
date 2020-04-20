list_nums = [round(float(i)) for i in input().split()]
print(min(list_nums))
print(max(list_nums))
d = sorted({i * 3 for i in list_nums})
print(*d)