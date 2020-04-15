hours = list(map(lambda x: int(x), input().split()))
num = 0

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'End':
        for i in range(len(hours)):
            if hours[i] > 0:
                print(hours[i], end=' ')
        exit()
    if command == 'Complete':
        index = int(cmd[1])
        if index <= len(hours) - 1 and index >= 0:
            hours[index] = 0
    elif command == 'Change':
        index = int(cmd[1])
        time = int(cmd[2])
        if index <= len(hours) - 1 and index >= 0:
            hours[index] = time
    elif command == 'Drop':
        index = int(cmd[1])
        if index <= len(hours) - 1 and index >= 0:
            hours[index] = -1
    elif command == 'Count' and cmd[1] == 'Completed':
        num = 0
        for i in range(len(hours)):
            if hours[i] == 0:
                num += 1
        print(num)
    elif command == 'Count' and cmd[1] == 'Incomplete':
        num = 0
        for i in range(len(hours)):
            if hours[i] > 0:
                num += 1
        print(num)
    elif command == 'Count' and cmd[1] == 'Dropped':
        num = 0
        for i in range(len(hours)):
            if hours[i] == -1:
                num += 1
        print(num)