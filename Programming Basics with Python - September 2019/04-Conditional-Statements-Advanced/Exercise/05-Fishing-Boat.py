budget = float(input())
season = input()
fishermans = float(input())
ship_cost = 0

if season == 'Spring':
    ship_cost = 3000
    if fishermans <= 6:
        ship_cost *= 0.9
    elif fishermans <= 11:
        ship_cost *= 0.85
    else:
        ship_cost *= 0.75

    if  fishermans % 2 == 0:
        ship_cost *= 0.95
elif season == 'Summer':
    ship_cost = 4200
    if fishermans <= 6:
        ship_cost *= 0.9
    elif fishermans <= 11:
        ship_cost *= 0.85
    else:
        ship_cost *= 0.75

    if  fishermans % 2 == 0:
        ship_cost *= 0.95
elif season == 'Autumn':
    ship_cost = 4200
    if fishermans <= 6:
        ship_cost *= 0.9
    elif fishermans <= 11:
        ship_cost *= 0.85
    else:
        ship_cost *= 0.75
elif season == 'Winter':
    ship_cost = 2600
    if fishermans <= 6:
        ship_cost *= 0.9
    elif fishermans <= 11:
        ship_cost *= 0.85
    else:
        ship_cost *= 0.75

    if  fishermans % 2 == 0:
        ship_cost *= 0.95

if budget >= ship_cost:
    money_left = budget - ship_cost
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = ship_cost - budget
    print(f'Not enough money! You need {money_needed:.2f} leva.')