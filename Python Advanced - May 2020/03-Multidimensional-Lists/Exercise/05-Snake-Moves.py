def append_snake(reverse, snake, row, inx):
    for column in range(columns):
        if inx >= len(snake):
            inx = 0
        if reverse:
            matrix[row-1].insert(0, snake[inx])
        else:
            matrix[row-1].append(snake[inx])
        inx += 1

    return inx


rows, columns = map(int, input().split())
snake_str = input()
matrix = [[] for i in range(rows)]
reverse = False
indexes = 0

for i in range(1, rows+1):
    if i % 2 == 1:
        reverse = False
    elif i % 2 == 0:
        reverse = True
    indexes = append_snake(reverse, snake_str, i, indexes)

[print(*i, sep='') for i in matrix]