d = {}
d_two = {}

while True:
    cmd = input()
    if cmd == 'Season end':
        break
    if ' -> ' in cmd:
        cmd = cmd.split(' -> ')
        player = cmd[0]
        position = cmd[1]
        skill = int(cmd[2])
        if player not in d:
            d[player] = skill
            d_two[player] = {position: skill}
        elif player in d:
            if position in d_two[player]:
                if skill > d_two[player][position]:
                    d[player] += skill - d_two[player][position]
                    d_two[player][position] = skill
            else:
                d_two[player].update({position: skill})
                d[player] += skill
    elif ' vs ' in cmd:
        cmd = cmd.split(' vs ')
        player_one = cmd[0]
        player_two = cmd[1]
        if player_one in d and player_two in d:
            fight = False
            l = [i for i in d_two[player_one].keys()]
            l_two = {i for i in d_two[player_two].keys()}
            for i in l:
                if i in l_two:
                    fight = True
                    break
            if fight:
                if d[player_one] > d[player_two]:
                    d.pop(player_two)
                    d_two.pop(player_two)
                elif d[player_one] < d[player_two]:
                    d.pop(player_one)
                    d_two.pop(player_one)

var = {}
sorted_d = dict(sorted(d.items(), key=lambda x: (-x[1], x[0])))
for i in d_two:
    hui = d_two[i]
    hui_sorted = dict(sorted(hui.items(), key=lambda x: (-x[1], x[0])))
    var.update({i: hui_sorted})

for k,v in sorted_d.items():
    print(f'{k}: {v} skill')
    for key, value in var[k].items():
        print(f'- {key} <::> {value}')