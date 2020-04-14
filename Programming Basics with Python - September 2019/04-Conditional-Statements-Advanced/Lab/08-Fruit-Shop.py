fruit = input()
day_of_week = input()
amount = float(input())
den = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

if day_of_week == den[0] or day_of_week == den[1] or day_of_week == den[2] or day_of_week == den[3] or day_of_week == den[4]:
    if fruit == 'banana':
        price = 2.50
        print(f'{price * amount:.2f}')
    elif fruit == 'apple':
        price = 1.20
        print(f'{price * amount:.2f}')
    elif fruit == 'orange':
        price = 0.85
        print(f'{price * amount:.2f}')
    elif fruit == 'grapefruit':
        price = 1.45
        print(f'{price * amount:.2f}')
    elif fruit == 'kiwi':
        price = 2.70
        print(f'{price * amount:.2f}')
    elif fruit == 'pineapple':
        price = 5.50
        print(f'{price * amount:.2f}')
    elif fruit == 'grapes':
        price = 3.85
        print(f'{price * amount:.2f}')
    else:
        print('error')
elif day_of_week == den[5] or day_of_week == den[6]:
    if fruit == 'banana':
        price = 2.70
        print(f'{price * amount:.2f}')
    elif fruit == 'apple':
        price = 1.25
        print(f'{price * amount:.2f}')
    elif fruit == 'orange':
        price = 0.90
        print(f'{price * amount:.2f}')
    elif fruit == 'grapefruit':
        price = 1.60
        print(f'{price * amount:.2f}')
    elif fruit == 'kiwi':
        price = 3
        print(f'{price * amount:.2f}')
    elif fruit == 'pineapple':
        price = 5.60
        print(f'{price * amount:.2f}')
    elif fruit == 'grapes':
        price = 4.20
        print(f'{price * amount:.2f}')
    else:
        print('error')
else:
    print('error')