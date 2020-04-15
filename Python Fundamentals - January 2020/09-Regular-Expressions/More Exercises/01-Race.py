import re
pattern_name = r'[A-Za-z]+'
pattern_digits = r'[0-9]'
inp_list = input().split(', ')
d = {}
nums = {
    1: 'st',
    2: 'nd',
    3: 'rd',
}

while True:
    inp = input()
    if inp == 'end of race':
        break
    reg_pattern_name = ''.join(re.findall(pattern_name, inp))
    if reg_pattern_name in inp_list:
        reg_pattern_distance = list(map(lambda x: int(x), re.findall(pattern_digits, inp)))
        if reg_pattern_name not in d:
            d[reg_pattern_name] = 0
        d[reg_pattern_name] += sum(reg_pattern_distance)

sorted_d = dict(sorted(d.items(), key=lambda x: -x[1]))
counter = 1
for k,v in sorted_d.items():
    if counter > 3:
        exit()
    print(f'{counter}{nums[counter]} place: {k}')
    counter += 1