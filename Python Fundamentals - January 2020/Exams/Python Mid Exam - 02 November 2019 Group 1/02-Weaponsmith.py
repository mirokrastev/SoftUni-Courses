inp = input().split('|')
var = []
while True:
    command = input().split()
    if command[0] == 'Done':
        break
    elif command[0] == 'Move':
        if command[1] == 'Left':
            if int(command[2]) <= int(len(inp)) - 1 and int(command[2]) >= 1:
                inp[int(command[2])], inp[int(command[2]) - 1] = inp[int(command[2]) - 1], inp[int(command[2])]
        elif command[1] == 'Right':
            if int(command[2]) < int(len(inp)) - 1:
                inp[int(command[2])], inp[int(command[2]) + 1] = inp[int(command[2]) + 1], inp[int(command[2])]
    elif command[0] == 'Check':
        if command[1] == 'Even':
            var = []
            for i in range(0, len(inp) - 1):
                if i % 2 == 0:
                    var.append(inp[i])
            print(*var, sep=' ')
        elif command[1] == 'Odd':
            var = []
            for i in range(1, len(inp)):
                if i % 2 != 0:
                    var.append(inp[i])
            print(*var, sep=' ')
print(f'You crafted {"".join(inp)}!')