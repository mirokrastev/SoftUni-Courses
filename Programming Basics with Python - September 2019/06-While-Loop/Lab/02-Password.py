username = input()
psw = input()
psw_input = input()

while psw_input != psw:
    psw_input = input()

print(f'Welcome {username}!')