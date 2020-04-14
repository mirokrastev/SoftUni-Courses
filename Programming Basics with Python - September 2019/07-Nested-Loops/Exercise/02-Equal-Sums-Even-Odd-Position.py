a = int(input())
b = int(input())

for num in range(a,b+1):
    num = str(num)

    first_num = int(num[0])
    second_num = int(num[1])
    third_num = int(num[2])
    fourth_num = int(num[3])
    fifth_num = int(num[4])
    sixth_num = int(num[5])

    odd_pos_sum = fifth_num + first_num + third_num
    even_pos_sum = second_num + fourth_num + sixth_num
    are_equal = odd_pos_sum == even_pos_sum

    if are_equal:
        print(num, end=' ')