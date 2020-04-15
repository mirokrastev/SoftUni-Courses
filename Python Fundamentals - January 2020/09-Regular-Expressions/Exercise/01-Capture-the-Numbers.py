import re
while True:
    try:
        inp = input()
        pattern = r'\d+'
        reg = re.findall(pattern, inp)
        if reg:
            print(*reg, end=' ')
    except:
        exit()