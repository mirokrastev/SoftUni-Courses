inp = list(map(lambda x: int(x), input().split()))

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'END':
        print(*inp, sep=' ')
        exit()
    if command == 'Change':
        painting_num = int(cmd[1])
        changed_num = int(cmd[2])
        if painting_num in inp:
            inp[inp.index(painting_num)] = changed_num
    elif command == 'Hide':
        painting_num = int(cmd[1])
        if painting_num in inp:
            inp.pop(inp.index(painting_num))
    elif command == 'Switch':
        painting_num = int(cmd[1])
        painting_num_two = int(cmd[2])
        if all([painting_num in inp, painting_num_two in inp]):
            index_one = inp.index(painting_num)
            index_two = inp.index(painting_num_two)
            inp[index_one], inp[index_two] = inp[index_two], inp[index_one]
    elif command == 'Insert':
        place = int(cmd[1]) + 1
        painting_num = int(cmd[2])
        if place <= len(inp) - 1 and place >= 0:
            inp.insert(place, painting_num)
    elif command == 'Reverse':
        inp.reverse()