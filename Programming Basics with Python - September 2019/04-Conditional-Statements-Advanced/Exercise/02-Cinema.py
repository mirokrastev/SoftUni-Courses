projection = input()
rows = int(input())
columns = int(input())

if projection == 'Premiere':
    price = 12
    total_sum = price * rows * columns
    print(f'{total_sum:.2f}')
elif projection == 'Normal':
    price = 7.50
    total_sum = price * rows * columns
    print(f'{total_sum:.2f}')
elif projection == 'Discount':
    price = 5
    total_sum = price * rows * columns
    print(f'{total_sum:.2f}')