d = {}
d_two = {}

while True:
    cmd = input().split(':')
    command = cmd[0]
    if command == 'Last Info':
        sorted_d_two = sorted(d_two.items(), key=lambda x: (-x[1], x[0]))
        print('Animals:')
        for i in sorted_d_two:
            print(f'{i[0]} -> {i[1]}g')
        print('Areas with hungry animals:')
        sorted_d = sorted(d.items(), key=lambda x: -x[1])
        for i in sorted_d:
            print(f'{i[0]} : {i[1]}')
        exit()
    if command == 'Add':
        animal_name = cmd[1]
        daily_food_limit = int(cmd[2])
        area = cmd[3]
        if area not in d:
            d[area] = 1
        elif area in d and animal_name not in d_two:
            d[area] += 1
        if animal_name not in d_two:
            d_two[animal_name] = daily_food_limit
        elif animal_name in d_two:
            d_two[animal_name] += daily_food_limit
    elif command == 'Feed':
        animal_name = cmd[1]
        food = int(cmd[2])
        area = cmd[3]
        if animal_name not in d_two:
            d_two[animal_name] = food
            if area not in d:
                d[area] = 1
            elif area in d:
                d[area] += 1
            d_two[animal_name] -= food
            if d_two[animal_name] <= 0:
                del d_two[animal_name]
                d[area] -= 1
                if d[area] == 0:
                    del d[area]
            continue
        if animal_name in d_two:
            d_two[animal_name] -= food
        if d_two[animal_name] <= 0:
            print(f'{animal_name} was successfully fed')
            del d_two[animal_name]
            d[area] -= 1
            if d[area] == 0:
                del d[area]