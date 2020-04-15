from re import findall
input = input()
pattern = '\\b[A-Z]{1}[a-z]+[ ][A-Z]{1}[a-z]+\\b'
reg = findall(pattern, input)
print(*reg, sep=' ')