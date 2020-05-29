def add_matrix():
    arg = [int(i) for i in input().split()]
    matrix.append(arg)


def detonate_bombs(coordinate):
    row, col = map(int, coordinate.split(','))
    if matrix[row][col] >= 1:
        value = matrix[row][col]
        matrix[row][col] -= value
        coordinates_var = coordinates_func(row, col)
        for k,v in coordinates_var.values():
            if k <= -1 or v <= -1:
                continue
            try:
                if matrix[k][v] >= 1:
                    matrix[k][v] -= value
            except: pass


def coordinates_func(row, col):
    return {
        0: (row-1, col-1),
        1: (row-1, col),
        2: (row-1, col+1),
        3: (row, col-1),
        4: (row, col+1),
        5: (row+1, col-1),
        6: (row+1, col),
        7: (row+1, col+1)
    }


rows_columns = int(input())
matrix = []
[add_matrix() for i in range(rows_columns)]
coordinates_inp = input().split()
[detonate_bombs(i) for i in coordinates_inp]
alive_cells = 0
sum_alive_cells = 0

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] >= 1:
            alive_cells += 1
            sum_alive_cells += matrix[row][col]

print(f'Alive cells: {alive_cells}')
print(f'Sum: {sum_alive_cells}')
[print(*i, sep=' ') for i in matrix]