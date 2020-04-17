inp = input()
s = []
valid = True
pairs = {
    '{': '}',
    '[': ']',
    '(': ')',
}

for i in inp:
    if i in '({[':
        s.append(i)
    elif i in ')}]':
        if s:
            current = s[-1]
            if pairs[current] == i:
                s.pop()
            else:
                valid = False
                break
        else:
            valid = False
            break

print('YES') if valid else print("NO")