d = {}
individualists = {}
var = {}

while True:
    cmd = input().split(' -> ')
    if cmd[0] == 'no more time':
        break
    username = cmd[0]
    contest = cmd[1]
    points = int(cmd[2])
    if contest not in d:
        d[contest] = {}
    if username not in d[contest]:
        d[contest].update({username: points})
    elif username in d[contest]:
        if points > d[contest][username]:
            individualists[username] += points - d[contest][username]
            d[contest][username] = points
            continue
        elif points <= d[contest][username]:
            continue
    if username not in individualists:
        individualists[username] = 0
    individualists[username] += points

for i in d:
    hui = d[i]
    sorted_hui = sorted(hui.items(), key=lambda x: (-x[1], x[0]))
    var.update({i: dict(sorted_hui)})

for i in d:
    print(f'{i}: {len(d[i])} participants')
    counter = 1
    for k, v in var[i].items():
        print(f'{counter}. {k} <::> {v}')
        counter += 1
counter = 1
sorted_individualists = dict(sorted(individualists.items(), key=lambda x: (-x[1], x[0])))
print('Individual standings:')
for k,v in sorted_individualists.items():
    print(f'{counter}. {k} -> {v}')
    counter += 1