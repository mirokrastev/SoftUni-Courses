initial_list = input().split('!')

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Go':
        print(*initial_list, sep=', ')
        exit()
    if command == 'Urgent':
        item = cmd[1]
        if item not in initial_list:
            initial_list.insert(0, item)
    elif command == 'Unnecessary':
        item = cmd[1]
        if item in initial_list:
            initial_list.remove(item)
    elif command == 'Correct':
        oldItem = cmd[1]
        newItem = cmd[2]
        if oldItem in initial_list:
            initial_list[initial_list.index(oldItem)]= newItem
    elif command == 'Rearrange':
        item = cmd[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)