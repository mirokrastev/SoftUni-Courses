from re import findall
inp = input()
pattern = r'\+359[ ]2[ ]\d{3}[ ]\d{4}|\+359-2-\d{3}-\d{4}\b'
reg = findall(pattern, inp)
print(*reg, sep=', ')