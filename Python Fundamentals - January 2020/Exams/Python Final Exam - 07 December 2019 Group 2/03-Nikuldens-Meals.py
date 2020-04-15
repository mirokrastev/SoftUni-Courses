d = {}
unliked_meals = 0

while True:
    cmd = input().split('-')
    command = cmd[0]
    if command == 'Stop':
        break
    if command == 'Like':
        guest = cmd[1]
        meal = cmd[2]
        if guest not in d:
            d[guest] = []
        if meal not in d[guest]:
            d[guest].append(meal)
    elif command == 'Unlike':
        guest = cmd[1]
        meal = cmd[2]
        if guest not in d:
            print(f'{guest} is not at the party.')
            continue
        if meal not in d[guest]:
            print(f'{guest} doesn\'t have the {meal} in his/her collection.')
            continue
        d[guest].remove(meal)
        unliked_meals += 1
        print(f'{guest} doesn\'t like the {meal}.')

sorted_d = dict(sorted(d.items(), key=lambda x: (-len(x[1]), x[0])))

for k,v in sorted_d.items():
    print(f'{k}: {", ".join(v)}')
print(f'Unliked meals: {unliked_meals}')