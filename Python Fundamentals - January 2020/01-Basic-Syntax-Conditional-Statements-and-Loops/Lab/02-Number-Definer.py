a = float(input())

if a == 0:
    print('zero')
    exit()
elif a > 0:
    if a < 1:
        print('small positive')
        exit()
    if a > 1000000:
        print('large positive')
        exit()
    else:
        print('positive')
        exit()
elif a < 0:
    if a > -1:
        print('small negative')
        exit()
    if a < -1000000:
        print('large negative')
        exit()
    else:
        print('negative')
        exit()