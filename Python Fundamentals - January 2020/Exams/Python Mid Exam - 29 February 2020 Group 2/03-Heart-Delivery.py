inp = list(map(lambda x: int(x), input().split('@')))
last_pos = 0
counter = 0

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Jump':
        lenght = int(cmd[1]) + last_pos
        if lenght <= len(inp) - 1 and lenght >= 1:
            if inp[lenght] == 0:
                print(f'Place {lenght} already had Valentine\'s day.')
                last_pos = lenght
                continue
            inp[lenght] -= 2
            if inp[lenght] == 0:
                print(f'Place {lenght} has Valentine\'s day.')
            last_pos = lenght
        else:
            if inp[0] == 0:
                print(f'Place {0} already had Valentine\'s day.')
                last_pos = 0
                continue
            inp[0] -= 2
            if inp[0] == 0:
                print(f'Place {0} has Valentine\'s day.')
            last_pos = 0
    elif command == 'Love!':
        print(f'Cupid\'s last position was {last_pos}.')
        if sum(inp) == 0:
            print(f'Mission was successful.')
            exit()
        else:
            for i in range(len(inp)):
                if inp[i] != 0:
                    counter += 1
            print(f'Cupid has failed {counter} places.')
            exit()