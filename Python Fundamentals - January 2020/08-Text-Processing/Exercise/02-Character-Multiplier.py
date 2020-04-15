string = input().split()
d = 0
min_num_cikul = min(len(string[0]), len(string[1]))
max_num_cikul = max(len(string[0]), len(string[1]))
for i in range(min_num_cikul):
    char_one = ord(string[0][i])
    char_two = ord(string[1][i])
    d += char_one * char_two

for l in range(min_num_cikul, max_num_cikul):
    if len(string[0]) > len(string[1]):
        d += ord(string[0][l])
    else:
        d += ord(string[1][l])
print(d)