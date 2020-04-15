exp_needed = float(input())
count_battles = int(input())
xp = 0

for i in range(1, count_battles + 1):
    exp_per_battle = float(input())
    if i % 3 == 0:
        exp_per_battle *= 1.15
    if i % 5 == 0:
        exp_per_battle *= 0.9
    xp += exp_per_battle
    if xp >= exp_needed:
        print(f'Player successfully collected his needed experience for {i} battles.')
        exit()
print(f'Player was not able to collect the needed experience, {exp_needed - xp:.2f} more needed.')