days_of_adventure = int(input())
count_players = int(input())
group_energy = float(input())
water_per_day_onep = float(input())
food_per_day_onep = float(input())
total_water = days_of_adventure * water_per_day_onep * count_players
total_food = days_of_adventure * food_per_day_onep * count_players

for i in range(1, days_of_adventure+1):
    energy_loss = float(input())
    group_energy -= energy_loss
    if group_energy <= 0:
        print(f'You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.')
        exit()
    if i % 2 == 0:
        group_energy *= 1.05
        total_water *= 0.7
    if i % 3 == 0:
        total_food -= total_food / count_players
        group_energy *= 1.10

print(f'You are ready for the quest. You will be left with - {group_energy:.2f} energy!')