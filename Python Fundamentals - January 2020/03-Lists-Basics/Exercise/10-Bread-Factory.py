orders = input().replace('-', '|').split('|')
initial_energy = 100
initial_coins = 100
counter = 1
garbage_collector = ''
for i in orders:
    if counter % 2 == 0:
        i = int(i)
        orders.insert(counter-1, [garbage_collector, i])
        orders.pop(counter)
    else:
        garbage_collector = i
    counter += 1
counter = 0
for _ in orders:
    if _ != type(list):
        orders.pop(counter)
    counter += 1
for l in range(len(orders)):
    if orders[l][0] == 'rest':
        counter = 0
        for _ in range(orders[l][1]):
            if initial_energy == 100:
                break
            counter += 1
            initial_energy += 1
        print(f'You gained {counter} energy.')
        print(f'Current energy: {initial_energy}.')
    elif orders[l][0] == 'order':
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += orders[l][1]
            print(f'You earned {orders[l][1]} coins.')
        else:
            initial_energy += 50
            print('You had to rest!')
    else:
        if initial_coins - orders[l][1] > 0:
            initial_coins -= orders[l][1]
        else:
            print(f'Closed! Cannot afford {orders[l][0]}.')
            exit()
        print(f'You bought {orders[l][0]}.')
print('Day completed!')
print(f'Coins: {initial_coins}')
print(f'Energy: {initial_energy}')