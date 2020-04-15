gifts = input().split()

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'No':
        try:
            for i in range(len(gifts)):
                gifts.remove('None')
        except:
            pass
        print(*gifts, sep=' ')
        exit()
    if command == 'OutOfStock':
        gift = cmd[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = 'None'
    elif command == 'Required':
        gift = cmd[1]
        index = int(cmd[2])
        if index <= len(gifts) - 1 and index >= 0:
            gifts[index] = gift
    elif command == 'JustInCase':
        gift = cmd[1]
        gifts[-1] = gift