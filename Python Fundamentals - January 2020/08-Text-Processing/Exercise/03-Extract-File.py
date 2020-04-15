inp = ''.join(reversed(input()))
extension = ''
name = ''
not_dot = False
for i in inp:
    if i == '.':
        not_dot = True
    while i != '.' and not not_dot:
        extension += i
        break
    while True and not_dot:
        if i == '.':
            break
        if i == '\\' or i == '\\\\':
            print(f'File name: {"".join(reversed(name))}')
            print(f'File extension: {"".join(reversed(extension))}')
            exit()
        name += i
        break