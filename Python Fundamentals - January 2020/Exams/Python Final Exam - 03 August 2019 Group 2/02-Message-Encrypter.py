import re
num = int(input())
pattern = r'(\*|\@)([A-Z][a-z]{2,})\1: \[([A-Za-z])\]\|\[([A-Za-z])\]\|\[([A-Za-z])\]\|$'

for i in range(num):
    #inp = input()
    reg = re.search(pattern, input())
    if reg:
        msg = reg.group(2)
        index_first = ord(reg.group(3))
        index_second = ord(reg.group(4))
        index_third = ord(reg.group(5))

        print(f'{msg}: {index_first} {index_second} {index_third}')
    else:
        print('Valid message not found!')