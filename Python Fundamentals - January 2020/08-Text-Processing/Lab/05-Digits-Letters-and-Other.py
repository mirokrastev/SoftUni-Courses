inp_raw = input()
digits = ''
letters = ''
other = ''
for i in inp_raw:
    if i.isnumeric():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        other += i
print(digits)
print(letters)
print(other)