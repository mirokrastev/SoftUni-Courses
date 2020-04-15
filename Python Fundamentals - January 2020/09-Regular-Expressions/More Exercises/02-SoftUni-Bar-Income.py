import re
pattern_custm_name_one = r'(?<=%)[A-Z][a-z]+(?=%)'
pattern_product_two = r'(?<=<)\w+(?=>)'
pattern_count_three = r'(?<=\|)[0-9]+(?=\|)'
pattern_price_four = r'(?<=\|)([A-Za-z_]+)*([0-9]+(\.[0-9]+)*)\$'
var = 0

while True:
    inp = input()
    if inp == 'end of shift':
        var = round(var, 2)
        print(f'Total income: {var:.2f}')
        exit()
    reg_one = re.search(pattern_custm_name_one, inp)
    if reg_one:
        reg_two = re.search(pattern_product_two, inp)
        if reg_two:
            reg_three = re.search(pattern_count_three, inp)
            if reg_three:
                reg_four = re.search(pattern_price_four, inp)
                if reg_four:
                    sum = int(reg_three.group(0)) * float(reg_four.group(2))
                    print(f'{reg_one.group(0)}: {reg_two.group(0)} - {sum:.2f}')
                    var += sum