list_nums = list(map(int, input().split()))
remove_positive = sum(filter(lambda x: x < 0, list_nums))
print(abs(remove_positive))