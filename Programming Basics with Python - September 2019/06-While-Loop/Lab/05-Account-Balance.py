installments_count = int(input())
installments_made_counter = 0
total_money = 0

while installments_made_counter < installments_count:
    money = float(input())
    if money < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {money:.2f}')
    total_money += money
    installments_made_counter += 1

print(f'Total: {total_money:.2f}')