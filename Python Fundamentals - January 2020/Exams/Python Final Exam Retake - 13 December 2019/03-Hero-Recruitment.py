d = {}

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'End':
        break
    if command == 'Enroll':
        hero_name = cmd[1]
        if hero_name not in d:
            d[hero_name] = []
        else:
            print(f'{hero_name} is already enrolled.')
    elif command == 'Learn':
        hero_name = cmd[1]
        spell_name = cmd[2]
        if hero_name not in d:
            print(f'{hero_name} doesn\'t exist.')
            continue
        if spell_name in d[hero_name]:
            print(f'{hero_name} has already learnt {spell_name}.')
            continue
        d[hero_name].append(spell_name)
    elif command == 'Unlearn':
        hero_name = cmd[1]
        spell_name = cmd[2]
        if hero_name not in d:
            print(f'{hero_name} doesn\'t exist.')
            continue
        if spell_name not in d[hero_name]:
            print(f'{hero_name} doesn\'t know {spell_name}.')
            continue
        d[hero_name].remove(spell_name)

sorted_d = dict(sorted(d.items(), key=lambda x: (-len(x[1]), x[0])))
print('Heroes:')
for k,v in sorted_d.items():
    print(f'== {k}: {", ".join(v)}')