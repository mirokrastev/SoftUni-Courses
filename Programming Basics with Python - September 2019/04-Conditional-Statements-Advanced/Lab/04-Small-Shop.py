product = input()
town = input()
amount = float(input())
price = 0

if town == 'Sofia':
    if product == 'coffee':
        price = 0.50 * amount
    elif product == 'water':
        price = 0.80 * amount
    elif product == 'beer':
        price = 1.20 * amount
    elif product == 'sweets':
        price = 1.45 * amount
    elif product == 'peanuts':
        price = 1.60 * amount
elif town == 'Plovdiv':
    if product == 'coffee':
        price = 0.40 * amount
    elif product == 'water':
        price = 0.70 * amount
    elif product == 'beer':
        price = 1.15 * amount
    elif product == 'sweets':
        price = 1.30 * amount
    elif product == 'peanuts':
        price = 1.50 * amount
elif town == 'Varna':
    if product == 'coffee':
        price = 0.45 * amount
    elif product == 'water':
        price = 0.70 * amount
    elif product == 'beer':
        price = 1.10 * amount
    elif product == 'sweets':
        price = 1.35 * amount
    elif product == 'peanuts':
        price = 1.55 * amount
print(price)