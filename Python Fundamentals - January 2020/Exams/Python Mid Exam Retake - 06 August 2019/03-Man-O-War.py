status_pirate_ship = list(map(lambda x: int(x), input().split('>')))
status_warship = list(map(lambda x: int(x), input().split('>')))
max_health = int(input())
twenty_percent = max_health * 0.2
d = 0

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Retire':
        print(f'Pirate ship status: {sum(status_pirate_ship)}')
        print(f'Warship status: {sum(status_warship)}')
        exit()
    if command == 'Fire':
        index = int(cmd[1])
        damage = int(cmd[2])
        if index <= len(status_warship) - 1 and index >= 0:
            status_warship[index] -= damage
            if status_warship[index] <= 0:
                print('You won! The enemy ship has sunken.')
                exit()
    elif command == 'Defend':
        startIndex = int(cmd[1])
        endIndex = int(cmd[2])
        damage = int(cmd[3])
        if startIndex <= endIndex and startIndex <= len(status_pirate_ship) - 1 and startIndex >= 0 \
            and endIndex <= len(status_pirate_ship) - 1 and endIndex >= 0:
            for i in range(startIndex, endIndex + 1):
                status_pirate_ship[i] -= damage
                if status_pirate_ship[i] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    exit()
    elif command == 'Repair':
        index = int(cmd[1])
        health = int(cmd[2])
        if index <= len(status_pirate_ship) - 1 and index >= 0:
           if  status_pirate_ship[index] + health > max_health:
               status_pirate_ship[index] = max_health
           else:
               status_pirate_ship[index] += health
    elif command == 'Status':
        d = 0
        for i in range(len(status_pirate_ship)):
            if status_pirate_ship[i] < twenty_percent:
                d += 1
        print(f'{d} sections need repair.')