from re import findall
inp = input()

pattern = r'\b(\d{2})([\.\-\/])([A-Z][a-z]{2})\2(\d{4})\b'
reg = findall(pattern, inp)

for i in reg:
    print(f'Day: {i[0]}, Month: {i[2]}, Year: {i[3]}')