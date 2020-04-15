inp = input().split(', ')
b = []

for i in inp:
    if 3 <= len(i) <= 13:
        printer = True
        for l in i:
            if l.isnumeric() or l.isalpha() or l == '-' or l == '_' and l != '':
                printer = True
            else:
                printer = False
                break
        if printer:
            b.append(i)
print(*b, sep='\n')