d = [int(i) for i in input().split()]
print(list(filter(lambda x: x % 2 == 0, d)))