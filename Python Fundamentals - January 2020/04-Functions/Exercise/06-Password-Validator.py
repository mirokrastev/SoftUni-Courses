inp = input()
special_cases = ['!', '\'', '"', '#', '$', '@', '%', '^', '&', '*', '(', ')', '{', '}', '[', ']', ':', ',', '<', '.', '>', '/', '?', '|']
nums = [str(i) for i in range(10)]
def password_check(a):
    digits_two = False
    digits_letters = False
    counter = 1
    if 6 <= len(a) <= 10:
        lenght = True
    else:
        lenght = False
    for l in special_cases:
        if l in a:
            digits_letters = False
            break
        else:
            digits_letters = True
    for i in a:
        if i in nums:
            if counter >= 2:
                digits_two = True
                break
            else:
                digits_two = False
            counter += 1
        else:
            digits_two = False
    if digits_letters and lenght and digits_two:
        print('Password is valid')
    if not lenght:
        print('Password must be between 6 and 10 characters')
    if not digits_letters:
        print('Password must consist only of letters and digits')
    if not digits_two:
        print('Password must have at least 2 digits')
password_check(inp)