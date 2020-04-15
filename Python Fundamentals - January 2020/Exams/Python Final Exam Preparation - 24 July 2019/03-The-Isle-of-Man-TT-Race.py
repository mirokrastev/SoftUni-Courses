import re
pattern = r'(#|\$|%|&|\*)([A-Za-z]+)\1=([0-9]+)!!(.+)'

while True:
    inp = input()
    if inp == '':
        exit()
    reg = re.match(pattern, inp)
    if reg:
        if int(reg.group(3)) == len(reg.group(4)):
            d = ''
            for i in reg.group(4):
                d += chr(ord(i) + int(reg.group(3)))
            print(f'Coordinates found! {reg.group(2)} -> {d}')
            exit()
        else:
            print('Nothing found!')
    else:
        print('Nothing found!')