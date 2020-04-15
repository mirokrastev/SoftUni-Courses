d = {}

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Log':
        break
    if command == 'New':
        username = cmd[2]
        if username not in d:
            d[username] = [0, 0]
    elif command == 'Like:':
        username = cmd[1][0:-1]
        count = int(cmd[2])
        if username not in d:
            d[username] = [count, 0]
        else:
            d[username][0] += count
    elif command == 'Comment:':
        username = cmd[1]
        if username not in d:
            d[username] = [0, 1]
        else:
            d[username][1] += 1
    elif command == 'Blocked:':
        username = cmd[1]
        if username in d:
            d.pop(username)
        else:
            print(f'{username} doesn\'t exist.')

print(f'{len(d)} followers')
sorted_d = dict(sorted(d.items(), key=lambda x: (-x[1][0], x[0])))

for k,v in sorted_d.items():
    print(f'{k}: {sum(v)}')