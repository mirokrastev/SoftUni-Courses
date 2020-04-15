first_d = {}
second_d = {}
var = {}
while True:
    first_inp = input().split(':')
    if first_inp[0] == 'end of contests':
        break
    contest = first_inp[0]
    password = first_inp[1]
    if contest not in first_d:
        first_d[contest] = password

while True:
    raw_inp = input().split('=>')
    if raw_inp[0] == 'end of submissions':
        break
    contest = raw_inp[0]
    password = raw_inp[1]
    username = raw_inp[2]
    points = int(raw_inp[3])
    if contest in first_d and password == first_d[contest]:
        if username not in second_d:
            second_d[username] = {}
            second_d[username].update({contest: points})
            continue
        elif username in second_d:
            if contest not in second_d[username]:
                second_d[username].update({contest: points})
                continue
            elif contest in second_d[username] and points > second_d[username][contest]:
                second_d[username][contest] = points

for i in second_d.keys():
    if not var:
        var.update({i: sum(second_d[i].values())})
        continue
    if max(second_d[i].values()) > sum(var.values()):
        var.clear()
        var[i] = sum(second_d[i].values())
for k, v in var.items():
    print(f'Best candidate is {k} with total {v} points.')
var.clear()
print('Ranking: ')
sorted_second_d = dict(sorted(second_d.items(), key=lambda x: x))
for i in sorted_second_d:
    hui = sorted_second_d[i]
    sorted_hui = sorted(hui.items(), key=lambda x: -x[1])
    var.update({i: dict(sorted_hui)})
for i in var:
    print(f'{i}')
    for k, v in var[i].items():
        print(f'#  {k} -> {v}')