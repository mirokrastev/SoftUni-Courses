n1 = int(input())
n2 = int(input())
operator = input()

if operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        result = n1+n2
        if result % 2 == 0:
            print(f'{n1} {operator} {n2} = {result} - even')
        elif result % 2 != 0:
            print(f'{n1} {operator} {n2} = {result} - odd')
    elif operator == '-':
        result = n1 - n2
        if result % 2 == 0:
            print(f'{n1} {operator} {n2} = {result} - even')
        elif result % 2 != 0:
            print(f'{n1} {operator} {n2} = {result} - odd')
    elif operator == '*':
        result = n1 * n2
        if result % 2 == 0:
            print(f'{n1} {operator} {n2} = {result} - even')
        elif result % 2 != 0:
            print(f'{n1} {operator} {n2} = {result} - odd')
elif operator == '/':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
        exit()
    result = n1 / n2
    print(f'{n1} / {n2} = {result:.2f}')
elif operator == '%':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
        exit()
    result = n1 % n2
    print(f'{n1} % {n2} = {result}')