import re
num = int(input())
pattern = r'(\$|%)([A-Z][a-z]{2,})\1: \[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|'

for i in range(num):
    inp = input()
    reg = re.fullmatch(pattern, inp)
    if reg:
        name = reg.group(2)
        index_one = int(reg.group(3))
        index_two = int(reg.group(4))
        index_three = int(reg.group(5))
        print(f'{name}: {chr(index_one)}{chr(index_two)}{chr(index_three)}')
    else:
        print('Valid message not found!')