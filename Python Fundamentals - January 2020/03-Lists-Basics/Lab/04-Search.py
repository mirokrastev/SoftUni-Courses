n = int(input())
special_word = ''
non_special_list = []
special_list = []

for i in range(n+1):
    inp = input()
    if i == 0:
        special_word = inp
        continue
    non_special_list.append(inp)
    if special_word in inp:
        special_list.append(inp)
print(non_special_list)
print(special_list)