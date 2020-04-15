words = input().split(', ')
string = input()
res_list = []

for a in words:
    if a in string:
        res_list.append(a)
print(res_list)