budget = float(input())
season = input()

if budget <= 100:
    if season == 'summer':
        budget *= 0.3
        pochivka = 'Camp'
    elif season == 'winter':
        budget *= 0.7
        pochivka = 'Hotel'
    print(f'Somewhere in Bulgaria\n{pochivka} - {budget:.2f}')
elif  budget <= 1000:
    if season == 'summer':
        budget *= 0.4
        pochivka = 'Camp'
    elif season == 'winter':
        budget *= 0.8
        pochivka = 'Hotel'
    print(f'Somewhere in Balkans\n{pochivka} - {budget:.2f}')
elif budget > 1000:
    budget *= 0.9
    print(f'Somewhere in Europe\nHotel - {budget:.2f}')