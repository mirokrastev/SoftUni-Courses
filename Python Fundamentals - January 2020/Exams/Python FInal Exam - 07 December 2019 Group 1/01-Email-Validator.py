email = input()
while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Complete':
        exit()
    if command == 'Make':
        second_command = cmd[1]
        if second_command == 'Upper':
            email = email.upper()
            print(email)
        elif second_command == 'Lower':
            email = email.lower()
            print(email)
    elif command == 'GetDomain':
        count = int(cmd[1])
        email_reversed = "".join(reversed(email))
        print("".join(reversed(email_reversed[:count])))
    elif command == 'GetUsername':
        if '@' in email:
            var = ''
            get_in = True
            for i in email:
                while get_in:
                    if i == '@':
                        get_in = False
                        break
                    var += i
                    break
                if not get_in:
                    print(var)
                    break
        else:
            print(f'The email {email} doesn\'t contain the @ symbol.')
    elif command == 'Replace':
        char = cmd[1]
        email = email.replace(char, '-')
        print(email)
    elif command == 'Encrypt':
        for i in email:
            print(f'{ord(i)}', end=' ')