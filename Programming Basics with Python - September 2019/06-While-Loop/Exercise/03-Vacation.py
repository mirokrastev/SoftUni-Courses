money_needed = float(input())
start_money = float(input())

total_days_counter = 0
spend_days_counter = 0

while True:
    action = input()
    money = float(input())
    total_days_counter += 1

    if action == 'spend':
        start_money -= money
        if start_money < 0:
            start_money = 0

        spend_days_counter += 1

    if spend_days_counter == 5:
        print(f"You can't save the money.\n{total_days_counter}")
        break

    elif action == 'save':
        spend_days_counter = 0
        start_money += money

        if start_money >= money_needed:
            print(f'You saved the money for {total_days_counter} days.')
            break