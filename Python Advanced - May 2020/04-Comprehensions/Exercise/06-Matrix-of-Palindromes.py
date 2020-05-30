rows, columns = map(int, input().split())
matrix = []

for row in range(rows):
    matrix.append([])
    for column in range(row, columns + row):
        word = f'{chr(row+97)}{chr(column+97)}{chr(row+97)}'
        matrix[-1].append(word)

[print(*i, sep=' ') for i in matrix]