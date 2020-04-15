string = input().split()
len_str = int(len(string) / 2)
num_faro_shuffles = int(input())
dumb_list = []
faro_shuffle = []
for _ in range(len_str):
    dumb_list.append(string[0])
    string.pop(0)

while num_faro_shuffles != 0:
    num_faro_shuffles -= 1
    for l in range(len_str):
        for i in range(1):
            faro_shuffle.append(dumb_list[0])
            dumb_list.pop(0)
        for b in range(1):
            faro_shuffle.append(string[0])
            string.pop(0)
    string = faro_shuffle
    if num_faro_shuffles != 0:
        for _ in range(len_str):
            dumb_list.append(string[0])
            string.pop(0)
print(faro_shuffle)