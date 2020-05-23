matrix = []

def add_matrix():
    arg = [int(i) for i in input().split()]
    matrix.append(arg)

def fn(matrix, bombs):
    for i in bombs:
        row, column = i
        if matrix[row][column] > 0:
            top = (row - 1, column)
            top_left = (row - 1, column - 1)
            top_right = (row - 1, column + 1)
            left = (row, column - 1)
            right = (row, column + 1)
            bottom = (row + 1, column)
            bottom_left = (row + 1, column - 1)
            bottom_right = (row + 1, column + 1)

            if row - 1 >= 0:
                if top[1] < len(matrix):
                    if matrix[top[0]][top[1]] > 0:
                        matrix[top[0]][top[1]] -= matrix[row][column]
                if top_left[1] >= 0:
                    if matrix[top_left[0]][top_left[1]] > 0:
                        matrix[top_left[0]][top_left[1]] -= matrix[row][column]
                if top_right[1] < len(matrix):
                    if matrix[top_right[0]][top_right[1]] > 0:
                        matrix[top_right[0]][top_right[1]] -= matrix[row][column]
            if row >= 0:
                if left[1] >= 0:
                    if matrix[left[0]][left[1]] > 0:
                        matrix[left[0]][left[1]] -= matrix[row][column]
                if right[1] < len(matrix):
                    if matrix[right[0]][right[1]] > 0:
                        matrix[right[0]][right[1]] -= matrix[row][column]
            if row + 1 < len(matrix):
                if bottom[1] < len(matrix):
                    if matrix[bottom[0]][bottom[1]] > 0:
                        matrix[bottom[0]][bottom[1]] -= matrix[row][column]
                if bottom_left[1] >= 0:
                    if matrix[bottom_left[0]][bottom_left[1]] > 0:
                        matrix[bottom_left[0]][bottom_left[1]] -= matrix[row][column]
                if bottom_right[1] < len(matrix):
                    if matrix[bottom_right[0]][bottom_right[1]] > 0:
                        matrix[bottom_right[0]][bottom_right[1]] -= matrix[row][column]
            matrix[row][column] = 0


square_matrix = int(input())

[add_matrix() for i in range(square_matrix)]
bombs = [[int(l) for l in i.split(',')] for i in input().split()]
fn(matrix, bombs)

the_sum = 0
active_cells = 0
for row in range(len(matrix)):
    for column in range(len(matrix)):
        if matrix[row][column] > 0:
            the_sum += matrix[row][column]
            active_cells += 1

print(f'Alive cells: {active_cells}')
print(f'Sum: {the_sum}')
[print(*i, sep=' ')for i in matrix]