single_num = input()
def number(a):
    odd_sum = 0
    even_sum = 0
    for i in single_num:
        i = int(i)
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')
number(single_num)