import re
num = int(input())
pattern = r'@\#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@\#+'

for i in range(num):
    inp = input()
    reg = re.fullmatch(pattern, inp)
    if reg:
        barcode = reg.group(1)
        to_print = ''
        for i in barcode:
            if i.isnumeric():
                to_print += i
        if not to_print:
            to_print = '00'
        print(f'Product group: {to_print}')
    else:
        print('Invalid barcode')