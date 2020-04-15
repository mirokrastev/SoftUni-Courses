num_cmds = int(input())
d = {}

for i in range(num_cmds):
    cmd = input().split()
    command = cmd[0]
    if command == 'register':
        username = cmd[1]
        licenseplate = cmd[2]
        if username not in d:
            d[username] = licenseplate
            print(f'{username} registered {licenseplate} successfully')
        elif username in d:
            print(f'ERROR: already registered with plate number {d[username]}')
    elif command == 'unregister':
        username = cmd[1]
        if username not in d:
            print(f'ERROR: user {username} not found')
        else:
            print(f'{username} unregistered successfully')
            d.pop(username)

for i in d:
    print(f'{i} => {d[i]}')