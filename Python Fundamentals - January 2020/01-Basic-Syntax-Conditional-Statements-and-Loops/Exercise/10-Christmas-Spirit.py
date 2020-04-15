quantity = int(input())
days = int(input())
quantity_reserved = quantity

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

christmas_spirit = 0
cost = 0

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        cost += ornament_set * quantity
        christmas_spirit += 5
    if i % 3 == 0:
        cost += (tree_skirt * quantity) + (tree_garlands * quantity)
        christmas_spirit += 13
    if i % 5 == 0:
        cost += tree_lights * quantity
        christmas_spirit += 17
        if i % 3 == 0:
            christmas_spirit += 30
    if i % 10 == 0:
        christmas_spirit -= 20
        cost += tree_skirt + tree_garlands + tree_lights
if i % 10 == 0:
    christmas_spirit -= 30

print(f'Total cost: {cost}')
print(f'Total spirit: {christmas_spirit}')