def add_matrix():
    arg = [i for i in input().split()]
    matrix.append(arg)


def find_square_matrices(coordinate):
    global square_matrices

    coordinate_list = list(coordinate.values())
    if list(coordinate_list[0] * 4) == coordinate_list:
        square_matrices += 1


rows, columns = [int(i) for i in input().split()]
matrix = []
[add_matrix() for i in range(rows)]
square_matrices = 0

for row in range(rows-1):
    for column in range(columns-1):
        coordinates = {
            0: matrix[row][column],
            1: matrix[row][column+1],
            2: matrix[row+1][column],
            3: matrix[row+1][column+1]
        }
        find_square_matrices(coordinates)

print(square_matrices)