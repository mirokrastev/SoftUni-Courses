import math

nums = list(map(int, input().split(', ')))
max_num = max(nums)
groups_count = math.ceil(max_num / 10)

for group in range(1, groups_count + 1):
    group_nums = []
    min = group * 10 - 10
    max = group * 10

    for num in nums:
        if min < num <= max:
            group_nums.append(num)

    print(f'Group of {group * 10}\'s: {group_nums}')