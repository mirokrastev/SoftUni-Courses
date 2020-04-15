a = input()
b = input()
prazno_1 = []
prazno_2 = []
counter = 0

for i in a:
    prazno_1.append(i)
for l in b:
    prazno_2.append(l)

asd = int((len(prazno_1) + len(prazno_2)) / 2)

for c in range(0, asd):
    counter += 1
    if not prazno_1[0:counter] == prazno_2[0:counter]:
        prazno_1.pop(c)
        prazno_1.insert(c, prazno_2[c])
        print(*prazno_1, sep='')