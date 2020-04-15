lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_broke_count = 0
sword_broke_count = 0
shield_broke_count = 0
armor_broke_count = 0

for i in range(1, lost_fights_count + 1):
    if i % 2 == 0:
        helmet_broke_count += 1
    if i % 3 == 0:
        sword_broke_count += 1
    if i % 2 == 0 and i % 3 == 0:
        shield_broke_count += 1
        if shield_broke_count % 2 == 0 and shield_broke_count != 0:
            armor_broke_count += 1

helmet_price_calc = helmet_broke_count * helmet_price
sword_price_calc = sword_broke_count * sword_price
shield_price_calc = shield_broke_count * shield_price
armor_price_calc = armor_broke_count * armor_price
result = helmet_price_calc + sword_price_calc + shield_price_calc + armor_price_calc
print(f'Gladiator expenses: {result:.2f} aureus')