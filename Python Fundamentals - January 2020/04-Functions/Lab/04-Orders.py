product = input()
quantity = int(input())
def producer(a,b):
    if product == 'water':
        cena = 1 * quantity
    elif product == 'coffee':
        cena = 1.5 * quantity
    elif product == 'coke':
        cena = 1.4 * quantity
    elif product == 'snacks':
        cena = 2 * quantity
    return f'{cena:.2f}'
print(producer(product, quantity))