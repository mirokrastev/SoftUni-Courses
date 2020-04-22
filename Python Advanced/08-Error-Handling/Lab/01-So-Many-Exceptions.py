numbers_list = [int(i) for i in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif number >= 6:
        result /= number

print(int(result))