d = {}

while True:
    cmd = input().split(' -> ')
    if cmd[0] == 'End':
        sorted_d = sorted(d.items(), key=lambda x: x[0])
        for i in sorted_d:
            print(f'{i[0]}')
            for l in i[1]:
                print(f'-- {l}')
        exit()
    company_name = cmd[0]
    employee_id = cmd[1]
    if company_name not in d:
        d[company_name] = [employee_id]
    elif all([company_name in d, employee_id not in d[company_name]]):
        d[company_name].append(employee_id)