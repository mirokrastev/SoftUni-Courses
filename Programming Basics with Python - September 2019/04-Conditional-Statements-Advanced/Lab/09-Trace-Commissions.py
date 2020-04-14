city = input()
sales_volume = float(input())
comission = 0

if city == 'Sofia' and sales_volume >= 0:
    if 0 <= sales_volume <= 500:
        comission = 5
    elif sales_volume <= 1000:
        comission = 7
    elif sales_volume <= 10000:
        comission = 8
    elif sales_volume > 10000:
        comission = 12
    print(f'{(comission / 100) * sales_volume:.2f}')
elif city == 'Varna' and sales_volume >= 0:
    if 0 <= sales_volume <= 500:
        comission = 4.5
    elif sales_volume <= 1000:
        comission = 7.5
    elif sales_volume <= 10000:
        comission = 10
    elif sales_volume > 10000:
        comission = 13
    print(f'{(comission / 100) * sales_volume:.2f}')
elif city == 'Plovdiv' and sales_volume >= 0:
    if 0 <= sales_volume <= 500:
        comission = 5.5
    elif sales_volume <= 1000:
        comission = 8
    elif sales_volume <= 10000:
        comission = 12
    elif sales_volume > 10000:
        comission = 14.5
    print(f'{(comission / 100) * sales_volume:.2f}')
else:
    print('error')