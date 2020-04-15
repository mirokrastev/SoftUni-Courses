import re
flat_pattern = r'([A-Za-z0-9\!\@\#\$\?]+)=([0-9]+)<<(.+)'

while True:
    inp = input()
    if inp == 'Last note':
        exit()
    flat_reg = re.match(flat_pattern, inp)
    if flat_reg:
        geohashcode_length = int(flat_reg.group(2))
        geohash_code = len(flat_reg.group(3))
        if geohash_code == geohashcode_length:
            name_mountain = flat_reg.group(1)
            appender = ''
            for i in name_mountain:
                if i.isalnum():
                    appender += i
            print(f'Coordinates found! {appender} -> {flat_reg.group(3)}')
        else:
            print('Nothing found!')
    else:
        print('Nothing found!')