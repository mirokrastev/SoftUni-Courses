def add_matrix():
    arg = [int(i) for i in input().split()]
    matrix.append(arg)


def submatrix(coordinate):
    global best_sum, best_submatrix
    sum_coordinates = sum(coordinate.values())
    if sum_coordinates > best_sum:
        best_sum = sum_coordinates
        best_submatrix = coordinate


matrix = []
rows, columns = [int(i) for i in input().split()]
[add_matrix() for i in range(rows)]
best_sum = -9999
best_submatrix = None

for row in range(rows-2):
    for column in range(columns-2):
        coordinates = {
            0: matrix[row][column],
            1: matrix[row][column+1],
            2: matrix[row][column+2],
            3: matrix[row+1][column],
            4: matrix[row+1][column+1],
            5: matrix[row+1][column+2],
            7: matrix[row+2][column],
            8: matrix[row+2][column+1],
            9: matrix[row+2][column+2],
        }
        submatrix(coordinates)

print(f'Sum = {best_sum}')
print('{} {} {}\n'
      '{} {} {}\n'
      '{} {} {}'.format(*best_submatrix.values()))