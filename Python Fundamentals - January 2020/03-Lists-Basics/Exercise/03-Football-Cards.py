string = input().split(' ')
d = []
team_a_calc = 11
team_b_calc = 11

for i in string:
    d.append(i)

d = sorted(set(d))
for l in d:
    if 'A' in l:
        team_a_calc -= 1
    if 'B' in l:
        team_b_calc -= 1
print(f'Team A - {team_a_calc}; Team B - {team_b_calc}')
if team_a_calc < 7 or team_b_calc < 7:
    print('Game was terminated')