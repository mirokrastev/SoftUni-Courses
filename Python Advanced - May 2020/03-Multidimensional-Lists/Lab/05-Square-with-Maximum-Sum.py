def add_matrix(): 
    arg = [int(i) for i in input().split(', ')]
    matrix.append(arg)


def submatrix(coordinate):
    global best_sum, best_submatrix
    sum_coordinates = sum(coordinate.values())

    if sum_coordinates > best_sum:
        best_sum = sum_coordinates
        best_submatrix = coordinate.values()


rows,columns = [int(i) for i in input().split(', ')]
matrix = []
[add_matrix() for i in range(rows)]
best_sum = 0
best_submatrix = None

for row in range(rows - 1):
    for column in range(columns - 1):
        coordinates = {
            0: matrix[row][column],
            1: matrix[row][column + 1],
            2: matrix[row + 1][column],
            3: matrix[row + 1][column + 1]
        }
        submatrix(coordinates)

print('{} {}\n'
      '{} {}'.format(*best_submatrix))
print(best_sum)