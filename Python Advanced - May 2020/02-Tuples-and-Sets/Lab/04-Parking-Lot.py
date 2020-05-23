def directions(arg, number):
    if arg == 'IN':
        cars.add(number)
    elif arg == 'OUT':
        if number in cars:
            cars.remove(number)


num = int(input())
cars = set()

for i in range(num):
    direction, number = input().split(', ')
    directions(direction, number)

[print(i) for i in cars] if cars else print('Parking Lot is Empty')