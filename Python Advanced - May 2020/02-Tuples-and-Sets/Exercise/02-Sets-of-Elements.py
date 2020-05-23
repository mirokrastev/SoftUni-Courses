s_one = set()
s_two = set()

first_set, second_set = [int(i) for i in input().split()]

for i in range(first_set):
    s_one.add(int(input()))

for i in range(second_set):
    s_two.add(int(input()))

[print(i) for i in s_one.intersection(s_two)]