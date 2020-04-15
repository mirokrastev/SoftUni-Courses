num_list = input().split(', ')
num_list = list(map(int, num_list))
num_beggars = int(input())
num_beggars_list = list(range(num_beggars))
counter = []
printer = []

for l in num_beggars_list:
    counter.append([])

while len(num_list) != 0:
    try:
        for i in range(len(counter)):
            counter[i].append(num_list[0])
            num_list.pop(0)
    except:
        continue

for b in range(len(counter)):
    if not counter[b]:
        counter[b].append(0)
    printer.append(sum(counter[b]))
print(printer)