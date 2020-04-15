inp = input().split(', ')
var = ''
while True:
    command = input().split()
    if command[0] == 'Report':
        break
    if command[0] == 'Blacklist':
        if command[1] in inp:
            for i in range(len(inp)):
                if command[1] == inp[i]:
                    inp[i] = 'Blacklisted'
                    print(f'{command[1]} was blacklisted.')
                    break
        else:
            print(f'{command[1]} was not found.')
    elif command[0] == 'Error':
        var = ''
        d = int(command[1])
        if 0 <= d <= len(inp) - 1:
            if inp[d] == 'Blacklisted' or inp[d] == 'Lost':
                continue
            else:
                var = inp[d]
                inp[d] = 'Lost'
                print(f'{var} was lost due to an error.')
    elif command[0] == 'Change':
        d = int(command[1])
        if 0 <= d <= len(inp) - 1:
            print(f'{inp[d]} changed his username to {command[2]}.')
            inp[d] = command[2]
print(f"Blacklisted names: {inp.count('Blacklisted')}")
print(f"Lost names: {inp.count('Lost')}")
print(*inp, sep=' ')