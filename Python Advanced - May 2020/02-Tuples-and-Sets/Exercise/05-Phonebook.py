d = {}


def add_phone(name, phone):
    if name not in d:
        d[name] = None
    d[name] = phone


def find_phone(name):
    if name in d:
        return f'{name} -> {d[name]}'
    return f'Contact {name} does not exist.'


while True:
    arg = input().split('-')
    if len(arg) == 1:
        num = int(arg[0])
        break
    else:
        name, phone = arg
        add_phone(name, phone)


for i in range(num):
    name = input()
    print(find_phone(name))