import re

pattern_name = r'((?<=U\$)[A-Z][a-z]{2,}(?=U\$))'
pattern_pass = r'((?<=P@\$)[A-Za-z]{5,}[0-9]+(?=P@\$))'
num = 0
count = int(input())
for x in range(count):
    reg = input()
    match = re.findall(pattern_name, reg)
    if match:
        match_two = re.findall(pattern_pass, reg)
        if match_two:
            print(f'Registration was successful')
            print(f'Username: {match[0]}, Password: {match_two[0]}')
            num += 1
        else:
            print(f'Invalid username or password')
    else:
        print(f'Invalid username or password')


print(f'Successful registrations: {num}')