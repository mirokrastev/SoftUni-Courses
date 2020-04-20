d = input().split()
filtered = list(filter(lambda x: x.isdigit(), d))
num = filter(lambda x: x > len(d), map(int, filtered))
print(*sorted(num))