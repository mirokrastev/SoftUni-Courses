import re
pattern = r'(#|\$|%|&|\*)([A-Za-z]+)\1=([0-9]+)!!(.+)'

while True:
    inp = input()
    if inp == '':
        exit()
    reg = re.match(pattern, inp)
    if reg:
        length_geohashcode = int(reg.group(3))
        encrypted_geohashcode = reg.group(4)
        if length_geohashcode == len(encrypted_geohashcode):
            name_racer = reg.group(2)
            decrypted_geohashcode = ''
            for i in encrypted_geohashcode:
                decrypted_geohashcode += chr(ord(i) + len(encrypted_geohashcode))
            print(f'Coordinates found! {name_racer} -> {decrypted_geohashcode}')
            exit()
        else:
            print('Nothing found!')
    else:
        print('Nothing found!')