import re
total_money = 0
furnitures = []
while True:
    inp = input()
    pattern = r'>>([A-Za-z0-9]+)<<([0-9]+\.?[0-9]+)!([0-9]+)'
    if inp == '':
        exit()
    if inp == 'Purchase':
        print('Bought furniture:')
        for i in furnitures:
            print(i)
        print(f'Total money spend: {total_money:.2f}')
        exit()
    reg = re.finditer(pattern, inp)
    for i in reg:
        furnitures.append(i.group(1))
        total_money += float(i.group(2)) * int(i.group(3))