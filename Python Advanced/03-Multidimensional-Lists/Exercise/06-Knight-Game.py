matrix = []

def add_matrix():
    arg = input()
    matrix.append([])
    [matrix[-1].append(i) for i in arg]

def make_indexes(row, column):
    two_v_up_one_h_left = (row - 2, column - 1)
    two_v_up_one_h_right = (row - 2, column + 1)
    one_v_up_two_h_left = (row - 1, column - 2)
    one_v_up_two_h_right = (row - 1, column + 2)
    one_v_down_two_h_left = (row + 1, column - 2)
    one_v_down_two_h_right = (row + 1, column + 2)
    two_v_down_one_h_left = (row + 2, column - 1)
    two_v_down_one_h_right = (row + 2, column + 1)

    return check_knight(
        two_v_up_one_h_left, two_v_up_one_h_right,
        one_v_up_two_h_left, one_v_up_two_h_right,
        one_v_down_two_h_left, one_v_down_two_h_right,
        two_v_down_one_h_left, two_v_down_one_h_right,
    )

def check_knight(a, b, c, d, e, f, g, h):
    hit_knight = 0
    if a[0] >= 0 and a[1] >= 0:
        (row, column) = a
        if matrix[row][column] == 'K':
            hit_knight += 1
    if b[0] >= 0 and b[1] < len(matrix):
        (row, column) = b
        if matrix[row][column] == 'K':
            hit_knight += 1
    if c[0] >= 0 and c[1] >= 0:
        (row, column) = c
        if matrix[row][column] == 'K':
            hit_knight += 1
    if d[0] >= 0 and d[1] < len(matrix):
        (row, column) = d
        if matrix[row][column] == 'K':
            hit_knight += 1
    if e[0] < len(matrix) and e[1] >= 0:
        (row, column) = e
        if matrix[row][column] == 'K':
            hit_knight += 1
    if f[0] < len(matrix) and f[1] < len(matrix):
        (row, column) = f
        if matrix[row][column] == 'K':
            hit_knight += 1
    if g[0] < len(matrix) and g[1] >= 0:
        (row, column) = g
        if matrix[row][column] == 'K':
            hit_knight += 1
    if h[0] < len(matrix) and h[1] < len(matrix):
        (row, column) = h
        if matrix[row][column] == 'K':
            hit_knight += 1

    return hit_knight

rows = int(input())
[add_matrix() for i in range(rows)]
position = tuple()
deleted_knights = 0

while True:
    result = 0
    for row in range(rows):
        for column in range(len(matrix)):
            current_index = matrix[row][column]
            if current_index == 'K':
                var = make_indexes(row, column)
                if var > result:
                    result = var
                    position = [row, column]

    if result == 0:
        break

    a, b = position
    matrix[a][b] = 'O'
    position.clear()
    deleted_knights += 1

print(deleted_knights)