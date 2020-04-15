inp = input().split(', ')
cmd_inp = int(input())

for i in range(cmd_inp):
    command = input().split(', ')
    if command[0] == 'Add':
        if command[1] in inp:
            print('Tank is already bought')
        else:
            inp.append(command[1])
            print('Tank successfully bought')
    elif command[0] == 'Remove':
        if command[1] in inp:
            inp.remove(command[1])
            print('Tank successfully sold')
        else:
            print('Tank not found')
    elif command[0] == 'Remove At':
        if 0 <= int(command[1]) <= len(inp) - 1:
            inp.pop(int(command[1]))
            print('Tank successfully sold')
        else:
            print('Index out of range')
    elif command[0] == 'Insert':
        if 0 <= int(command[1]) <= len(inp) - 1:
            if command[2] in inp:
                print('Tank is already bought')
            else:
                inp.insert(int(command[1]), command[2])
                print('Tank successfully bought')
        else:
            print('Index out of range')

print(*inp, sep=', ')