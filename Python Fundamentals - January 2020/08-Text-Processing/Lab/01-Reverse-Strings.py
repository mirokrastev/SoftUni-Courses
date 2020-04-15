while True:
    cmd = input()
    if cmd == 'end':
        exit()
    print(f'{cmd} = {"".join(list(reversed(cmd)))}')