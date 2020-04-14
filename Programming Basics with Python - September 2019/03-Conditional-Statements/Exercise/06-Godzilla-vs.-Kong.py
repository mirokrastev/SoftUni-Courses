budget = float(input())
stunts = int(input())
price_per_dreshka = float(input())

dekor = budget * 0.1
total_dreshki_price = price_per_dreshka * stunts

if stunts > 150:
    total_dreshki_price *= 0.9

total_sum = dekor + total_dreshki_price

if budget >= total_sum:
    print('Action!')
    money_left = budget - total_sum
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
elif total_sum > budget:
    print('Not enough money!')
    money_needed = total_sum - budget
    print(f'Wingard needs {money_needed:.2f} leva more.')