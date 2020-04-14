flowers = input()
flowers_number = int(input())
budget = int(input())
price = 0

if flowers == 'Roses':
    price = 5
    total_sum = flowers_number * price
    if flowers_number > 80:
        total_sum = total_sum * 0.9
    if total_sum > budget:
        leva_left = total_sum - budget
        print(f'Not enough money, you need {leva_left:.2f} leva more.')
    else:
        leva_left = budget - total_sum
        print(f'Hey, you have a great garden with {flowers_number} {flowers} and {leva_left:.2f} leva left.')
if flowers == 'Dahlias':
    price = 3.80
    total_sum = flowers_number * price
    if flowers_number > 90:
        total_sum = total_sum * 0.85
    if total_sum > budget:
        leva_left = total_sum - budget
        print(f'Not enough money, you need {leva_left:.2f} leva more.')
    else:
        leva_left = budget - total_sum
        print(f'Hey, you have a great garden with {flowers_number} {flowers} and {leva_left:.2f} leva left.')
if flowers == 'Tulips':
    price = 2.80
    total_sum = flowers_number * price
    if flowers_number > 80:
        total_sum = total_sum * 0.85
    if total_sum > budget:
        leva_left = total_sum - budget
        print(f'Not enough money, you need {leva_left:.2f} leva more.')
    else:
        leva_left = budget - total_sum
        print(f'Hey, you have a great garden with {flowers_number} {flowers} and {leva_left:.2f} leva left.')
if flowers == 'Narcissus':
    price = 3
    total_sum = flowers_number * price
    if flowers_number < 120:
        total_sum = total_sum * 1.15
    if total_sum > budget:
        leva_left = total_sum - budget
        print(f'Not enough money, you need {leva_left:.2f} leva more.')
    else:
        leva_left = budget - total_sum
        print(f'Hey, you have a great garden with {flowers_number} {flowers} and {leva_left:.2f} leva left.')
if flowers == 'Gladiolus':
    price = 2.50
    total_sum = flowers_number * price
    if flowers_number < 80:
        total_sum = total_sum * 1.20
    if total_sum > budget:
        leva_left = total_sum - budget
        print(f'Not enough money, you need {leva_left:.2f} leva more.')
    else:
        leva_left = budget - total_sum
        print(f'Hey, you have a great garden with {flowers_number} {flowers} and {leva_left:.2f} leva left.')