degrees = float(input())
time = input()
outfit = ""
shoes = ""

if time == 'Morning':
    if 10 <= degrees <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif time == 'Afternoon':
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degrees >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
elif time == 'Evening':
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= 25:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f'It\'s {degrees:.0f} degrees, get your {outfit} and {shoes}.')