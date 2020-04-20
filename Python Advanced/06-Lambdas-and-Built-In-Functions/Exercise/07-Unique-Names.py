import re
pattern = r'\b[A-Z][a-z]+\b'
inp = input()

reg = re.findall(pattern, inp)
print(sum([len(i) for i in reg]))