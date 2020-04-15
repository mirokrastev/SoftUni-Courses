import re
num = int(input())
pattern = r'(.+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|(.+)<\1'

for i in range(num):
    inp = input()
    reg = re.match(pattern, inp)
    if reg:
        first_group = reg.group(2)
        second_group = reg.group(3)
        third_group = reg.group(4)
        fourth_group = reg.group(5)
        print(f'Password: {first_group}{second_group}{third_group}{fourth_group}')
    else:
        print('Try another password!')