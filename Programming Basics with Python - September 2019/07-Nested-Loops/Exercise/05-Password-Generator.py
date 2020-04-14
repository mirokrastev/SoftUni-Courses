n = int(input())
l = int(input())
 
for symb1 in range(1, n + 1):
    for symb2 in range(1, n + 1):
        for symb3 in range(97, 97 + l):
            for symb4 in range(97, 97 + l):
                for symb5 in range(1, n + 1):
                    if symb5 > symb1 and symb5 > symb2:
                        print(f'{symb1}{symb2}{chr(symb3)}{chr(symb4)}{symb5} ',end = '')