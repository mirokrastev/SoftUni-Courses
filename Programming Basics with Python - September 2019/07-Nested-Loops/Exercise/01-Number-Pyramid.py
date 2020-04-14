n = int(input())
output = ''
counter = 0
is_found = False

for row in range(1, n+1):
    for column in range(1, row+1):
        counter += 1

        if row == column:
            output += f'{counter}\n'
        else:
            output += f'{counter} '
        if counter == n:
            is_found = True
            break
    if is_found:
        break
print(output)