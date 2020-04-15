input_string = input()
i = len(input_string)
s = ''

while i > 0:
    i -= 1
    s += input_string[i]

print(s)