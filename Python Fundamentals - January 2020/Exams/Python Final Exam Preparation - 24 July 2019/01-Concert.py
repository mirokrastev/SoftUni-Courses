import re
d = {}
d_two = {}
splitter = r'; |, '

while True:
    cmd = re.split(splitter, input())
    command = cmd[0]
    if command == 'start of concert':
        break
    if command == 'Add':
        band_name = cmd[1]
        members = cmd[2::]
        if band_name not in d:
            d[band_name] = []
        for i in members:
            if i not in d[band_name]:
                d[band_name].append(i)
    elif command == 'Play':
        band_name = cmd[1]
        time = int(cmd[2])
        if band_name not in d_two:
            d_two[band_name] = 0
        d_two[band_name] += time

group_end_inp = input()

print(f'Total time: {sum(d_two.values())}')
sorted_d_two = dict(sorted(d_two.items(), key=lambda x: (-x[1], x[0])))
for k,v in sorted_d_two.items():
    print(f'{k} -> {v}')

print(f'{group_end_inp}')
for v in d[group_end_inp]:
    print(f'=> {v}')