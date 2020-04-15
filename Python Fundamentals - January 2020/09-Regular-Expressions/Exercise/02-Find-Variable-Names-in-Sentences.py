from re import findall
inp = input()
pattern = r'\b_[A-Za-z0-9]+\b'
reg = [i.replace('_', '') for i in findall(pattern, inp)]
print(*reg, sep=',')