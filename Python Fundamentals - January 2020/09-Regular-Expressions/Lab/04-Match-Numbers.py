import re
inp = input()
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
reg = re.finditer(pattern, inp)
for i in reg:
    print(i.group(0), end=' ')