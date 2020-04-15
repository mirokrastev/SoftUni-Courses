d = {}

while True:
    cmd = input().split(':')
    command = cmd[0]
    if command == 'Results':
        break
    if command == 'Add':
        person_name = cmd[1]
        health = int(cmd[2])
        energy = int(cmd[3])
        if person_name not in d:
            d[person_name] = [health, energy]
        elif person_name in d:
            d[person_name][0] += health
    elif command == 'Attack':
        attacker_name = cmd[1]
        defender_name = cmd[2]
        damage = int(cmd[3])
        if attacker_name in d and defender_name in d:
            d[defender_name][0] -= damage
            d[attacker_name][1] -= 1
            if d[defender_name][0] <= 0:
                d.pop(defender_name)
                print(f'{defender_name} was disqualified!')
            if d[attacker_name][1] <= 0:
                d.pop(attacker_name)
                print(f'{attacker_name} was disqualified!')
    elif command == 'Delete':
        username = cmd[1]
        if username == 'All':
            d.clear()
            continue
        if username in d:
            d.pop(username)

print(f'People count: {len(d)}')
sorted_d = dict(sorted(d.items(), key=lambda x: (-x[1][0], x[0])))
for k,v in sorted_d.items():
    print(f'{k} - {v[0]} - {v[1]}')