d = input().split()
new_list = []

for i in range(len(d)):
    qwe = ''
    try:
        char = chr(int(d[i][0:3]))
        if len(d[i]) == 4:
            token = d[i][3]
            qwe = f'{char}{token}'
            new_list.append(qwe)
            continue
        elif len(d[i]) == 5:
            qwe = f'{char}{d[i][-1]}{d[i][-2]}'
            new_list.append(qwe)
            continue
        else:
            token = d[i][3]
            h = len(d[i]) - 4
            body = d[i][-h:-1]
            qwe = f'{char}{d[i][-1]}{body}{token}'
            new_list.append(qwe)
    except ValueError:
        char = chr(int(d[i][0:2]))
        if len(d[i]) == 3:
            token = d[i][2]
            qwe = f'{char}{token}'
            new_list.append(qwe)
            continue
        elif len(d[i]) == 4:
            qwe = f'{char}{d[i][-1]}{d[i][-2]}'
            new_list.append(qwe)
            continue
        else:
            token = d[i][2]
            h = len(d[i]) - 3
            body = d[i][-h:-1]
        qwe = f'{char}{d[i][-1]}{body}{token}'
        new_list.append(qwe)
print(*new_list, sep=' ')