d = {}

while True:
    cmd = input().split(' : ')
    if cmd[0] == 'end':
        for i in d:
            d[i].sort()
        sorted_d = sorted(d.items(), key=lambda x: len(x[1]), reverse=True)
        for i in sorted_d:
            print(f'{i[0]}: {len(i[1])}')
            for l in i[1]:
                print(f'-- {l}')
        exit()
    course_name = cmd[0]
    student_name = cmd[1]
    if course_name not in d:
        d[course_name] = [student_name]
    else:
        d[course_name].append(student_name)