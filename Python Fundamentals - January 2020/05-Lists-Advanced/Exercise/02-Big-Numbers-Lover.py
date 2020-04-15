numbers = [x for x in input().split()]
numbers.sort(reverse=True)
print(*numbers, sep='')