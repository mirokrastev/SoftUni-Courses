nums_inp = list(map(lambda x: int(x), input().split('|')))
point = 0

while True:
    cmd = input().split('@')
    command = cmd[0]
    if command == 'Game over':
        print(*nums_inp, sep=' - ')
        print(f'Iskren finished the archery tournament with {point} points!')
        exit()
    elif command == 'Reverse':
        nums_inp.reverse()
        continue
    start_index = int(cmd[1])
    lenght = int(cmd[2])
    if command == 'Shoot Left' and start_index <= (len(nums_inp) - 1) and start_index >= 0:
        for i in range(lenght):
            if start_index <= -len(nums_inp):
                start_index = 0
            start_index -= 1
        if nums_inp[start_index] < 5:
            point += nums_inp[start_index]
            nums_inp[start_index] = 0
        else:
            nums_inp[start_index] -= 5
            point += 5
    elif command == 'Shoot Right' and start_index <= (len(nums_inp) - 1) and start_index >= 0:
        for i in range(lenght):
            if start_index >= len(nums_inp):
                start_index = 0
            start_index += 1
        if nums_inp[start_index] < 5:
            point += nums_inp[start_index]
            nums_inp[start_index] = 0
        else:
            nums_inp[start_index] -= 5
            point += 5