import re
num = int(input())
pattern = r'\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#'

for i in range(num):
    inp = input()
    reg = re.match(pattern, inp)
    if reg:
        name = reg.group(1)
        title = reg.group(2)
        print(f'{name}, The {title}')
        print(f'>> Strength: {len(name)}')
        print(f'>> Armour: {len(title)}')
    else:
        print('Access denied!')