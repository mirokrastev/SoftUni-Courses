nums = list(map(lambda x: int(x), input().split()))

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'End':
        appender = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                appender.append(nums[i])
        print(*appender, sep=' ')
        exit()
    if command == 'Switch':
        index = int(cmd[1])
        if index <= len(nums) - 1 and index >= 0:
            nums[index] = -nums[index]
    elif command == 'Change':
        index = int(cmd[1])
        value = int(cmd[2])
        if index <= len(nums) - 1 and index >= 0:
            nums[index] = value
    elif command == 'Sum' and cmd[1] == 'Negative':
        appender = []
        for i in range(len(nums)):
            if nums[i] < 0:
                appender.append(nums[i])
        print((sum(appender)))
    elif command == 'Sum' and cmd[1] == 'Positive':
        appender = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                appender.append(nums[i])
        print(sum(appender))
    elif command == 'Sum' and cmd[1] == 'All':
        print(sum(nums))