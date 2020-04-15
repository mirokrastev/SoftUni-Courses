num_heroes = int(input())
heroes = {}

for i in range(num_heroes):
    heroes_inp = input().split()
    hero_name = heroes_inp[0]
    hp = int(heroes_inp[1])
    mp = int(heroes_inp[2])

    heroes[hero_name] = [hp, mp]

while True:
    cmd = input().split(' - ')
    command = cmd[0]
    if command == 'End':
        break
    if command == 'CastSpell':
        hero_name = cmd[1]
        mp_needed = int(cmd[2])
        spell_name = cmd[3]
        if hero_name in heroes:
            if mp_needed <= heroes[hero_name][1]:
                mana_point_left = heroes[hero_name][1] - mp_needed
                print(f'{hero_name} has successfully cast {spell_name} and now has {mana_point_left} MP!')
                heroes[hero_name][1] -= mp_needed
            else:
                print(f'{hero_name} does not have enough MP to cast {spell_name}!')
    elif command == 'TakeDamage':
        hero_name = cmd[1]
        damage = int(cmd[2])
        attacker = cmd[3]
        if hero_name in heroes:
            if heroes[hero_name][0] - damage <= 0:
                print(f'{hero_name} has been killed by {attacker}!')
                heroes.pop(hero_name)
            else:
                current_hp = heroes[hero_name][0] - damage
                print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!')
                heroes[hero_name][0] -= damage
    elif command == 'Recharge':
        hero_name = cmd[1]
        amount = int(cmd[2])
        if hero_name in heroes:
            if heroes[hero_name][1] + amount > 200:
                recharged = 0
                for i in range(amount):
                    if heroes[hero_name][1] >= 200:
                        break
                    else:
                        recharged += 1
                        heroes[hero_name][1] += 1
                print(f'{hero_name} recharged for {recharged} MP!')
            else:
                print(f'{hero_name} recharged for {amount} MP!')
                heroes[hero_name][1] += amount
    elif command == 'Heal':
        hero_name = cmd[1]
        amount = int(cmd[2])
        if hero_name in heroes:
            if heroes[hero_name][0] + amount > 100:
                recharged = 0
                for i in range(amount):
                    if heroes[hero_name][0] >= 100:
                        break
                    else:
                        recharged += 1
                        heroes[hero_name][0] += 1
                print(f'{hero_name} healed for {recharged} HP!')
            else:
                print(f'{hero_name} healed for {amount} HP!')
                heroes[hero_name][0] += amount

sorted_heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])))

for k,v in sorted_heroes.items():
    print(f'{k}')
    for l in v:
        print(f'  HP: {v[0]}')
        print(f'  MP: {v[1]}')
        break