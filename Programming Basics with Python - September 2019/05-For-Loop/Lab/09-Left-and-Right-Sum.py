numbers_count = int(input())
left_sum = 0
right_sum = 0

for index in range(numbers_count * 2):
    current_num = int(input())
    if index < numbers_count:
        left_sum += current_num
    else:
        right_sum += current_num

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')