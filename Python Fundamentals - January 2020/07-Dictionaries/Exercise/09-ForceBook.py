d = {}

while True:
    inp_raw = input()
    if inp_raw == 'Lumpawaroo':
        printer = sorted({i: d[i] for i in d if len(d[i]) != 0}.items(), key=lambda x: (-len(x[1]), x[0]))
        for i in range(len(printer)):
            print(f'Side: {printer[i][0]}, Members: {len(printer[i][1])}')
            printer_d = sorted(printer[i][1], key=lambda x: x)
            for l in printer_d:
                print(f'! {l}')
        exit()
    if ' | ' in inp_raw:
        cmd = inp_raw.split(' | ')
        force_side = cmd[0]
        force_user = cmd[1]
        printer = True
        for i in d:
            if force_user in d[i] and printer:
                printer = False
        if printer:
            if force_side not in d:
                d[force_side] = []
            if force_user not in d[force_side]:
                d[force_side].append(force_user)
    elif ' -> ' in inp_raw:
        cmd = inp_raw.split(' -> ')
        force_user = cmd[0]
        force_side = cmd[1]
        get_in = True
        try:
            for i in d:
                if force_user in d[i] and get_in:
                    d[i].remove(force_user)
                    if force_side not in d:
                        d[force_side] = []
                    d[force_side].append(force_user)
                    get_in = False
        except:
            pass
        if get_in:
            if force_side not in d:
                d[force_side] = []
            d[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')