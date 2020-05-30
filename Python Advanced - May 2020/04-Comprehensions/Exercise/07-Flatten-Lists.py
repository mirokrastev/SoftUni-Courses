inp_raw = list((reversed(input().replace(' ', 'a').split('|'))))
d = []
for i in inp_raw:
    d.extend([int(i) for i in i.split('a') if i != ''])

print(*d, sep=' ')