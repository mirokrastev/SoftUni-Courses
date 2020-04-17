def fn(rows, columns, snake):
    to_append = 0
    for i in range(rows):
        for l in range(columns):
            if to_append == len(snake):
                to_append = 0
            matrix[i].append(snake[to_append])
            to_append += 1

    for i in range(1, len(matrix) + 1):
        if i % 2 == 1:
            print("".join(matrix[i - 1]))
        else:
            print("".join(reversed(matrix[i - 1])))

rows, columns = list(map(int, input().split()))
snake = input()
matrix = [[] for i in range(rows)]
fn(rows, columns, snake)