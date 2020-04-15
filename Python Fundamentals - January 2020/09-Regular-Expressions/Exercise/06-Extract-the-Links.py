import re
pattern = r'(www\.[A-Za-z0-9-]+\.([a-z]\.?)+)'

while True:
    inp = input()
    if not inp:
        exit()
    reg = list(re.finditer(pattern, inp))
    for i in reg:
        print(i.group(1))