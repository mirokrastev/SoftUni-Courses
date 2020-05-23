d = {
    '{': '}',
    '[': ']',
    '(': ')'
}

arg = input()
s = []


def pairs(char, arg):
    if d[char] == arg:
        return True
    return False


for i in arg:
    if i in {'{', '[', '('}:
        s.append(i)
    elif i in {'}', ']', ')'}:
        if s:
            char = s.pop()
            if not pairs(char, i):
                print('NO')
                exit()
        else:
            print('NO')
            exit()

print('YES') if not s else print('NO')