d = {}

while True:
    cmd = input().split('->')
    command = cmd[0]
    if command == 'Statistics':
        break
    if command == 'Add':
        username = cmd[1]
        if username in d:
            print(f'{username} is already registered')
        else:
            d[username] = []
    elif command == 'Send':
        username = cmd[1]
        email = cmd[2]
        if username not in d:
            d[username] = []
        d[username].append(email)
    elif command == 'Delete':
        username = cmd[1]
        if username in d:
            d.pop(username)
        else:
            print(f'{username} not found!')

sorted_d = dict(sorted(d.items(), key=lambda x: (-len(x[1]), x[0])))
print(f'Users count: {len(sorted_d.keys())}')
for k,v in sorted_d.items():
    print(f'{k}')
    for l in v:
        print(f' - {l}')