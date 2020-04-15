journey_cost = float(input())
months = int(input())
money_saved = 0

for i in range(1, months+1):
    if i % 2 == 1 and i != 1:
        money_saved *= 0.84
    if i % 4 == 0:
        money_saved += money_saved * 0.25
    money_saved += journey_cost * 0.25

if money_saved > journey_cost:
    print(f'Bravo! You can go to Disneyland and you will have {money_saved-journey_cost:.2f}lv. for souvenirs.')
else:
    print(f'Sorry. You need {abs(money_saved-journey_cost):.2f}lv. more.')