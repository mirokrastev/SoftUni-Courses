d = {}
d_two = {}

while True:
    cmd = input().split('-')
    if cmd[0] == 'exam finished':
        sorted_d_two = sorted(d_two.items(), key=lambda x: (-x[1], x[0]))
        print('Results:')
        for i in sorted_d_two:
            print(f'{i[0]} | {i[1]}')
        print('Submissions:')
        sorted_d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        for i in sorted_d:
            print(f'{i[0]} - {i[1]}')
        exit()
    if 'banned' in cmd:
        username = cmd[0]
        if username in d_two:
            d_two.pop(username)
    else:
        username = cmd[0]
        language = cmd[1]
        points = int(cmd[2])
        if language not in d:
            d[language] = 0
        if username not in d_two:
            d_two[username] = points
        elif username in d_two and points > d_two[username]:
            d_two[username] = points
        d[language] += 1