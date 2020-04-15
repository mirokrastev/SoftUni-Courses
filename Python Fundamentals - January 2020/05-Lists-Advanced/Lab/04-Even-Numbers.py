nums = list(map(lambda x: int(x), input().split(', ')))
even_indices = [i for i in range(len(nums)) if nums[i] % 2 == 0]
print(even_indices)