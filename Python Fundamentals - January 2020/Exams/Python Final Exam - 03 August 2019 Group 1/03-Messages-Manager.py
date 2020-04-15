d = {}
capacity = int(input())

while True:
    cmd = input().split('=')
    command = cmd[0]
    if command == 'Statistics':
        break
    if command == 'Add':
        username = cmd[1]
        sent = int(cmd[2])
        received = int(cmd[3])
        if username not in d:
            d[username] = [sent, received]
    elif command == 'Message':
        sender = cmd[1]
        receiver = cmd[2]
        if sender in d and receiver in d:
            d[sender][0] += 1
            d[receiver][1] += 1
            if sum(d[sender]) >= capacity:
                d.pop(sender)
                print(f'{sender} reached the capacity!')
            if sum(d[receiver]) >= capacity:
                d.pop(receiver)
                print(f'{receiver} reached the capacity!')
    elif command == 'Empty':
        username = cmd[1]
        if username == 'All':
            d.clear()
            continue
        if username in d:
            d.pop(username)

sorted_d = dict(sorted(d.items(), key=lambda x: (-x[1][1], x[0])))
print(f'Users count: {len(sorted_d)}')
for k,v in sorted_d.items():
    print(f'{k} - {sum(v)}')