import re
num = int(input())
pattern = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'

for i in range(num):
    inp = input()
    reg = re.match(pattern, inp)
    if reg:
        name = reg.group(1)
        message = reg.group(2)
        d = [str(ord(i)) for i in message]
        print(f'{name}: {" ".join(d)}')
    else:
        print('The message is invalid')