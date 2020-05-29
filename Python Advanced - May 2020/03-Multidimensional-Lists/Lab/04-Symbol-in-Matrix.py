def add_matrix():
    arg = [i for i in input()]
    matrix.append(arg)


def find_symbol(row):
    for column in range(len(matrix)):
        if symbol == matrix[row][column]:
            print(f'({row}, {column})')
            exit()


rows_cols = int(input())
matrix = []
[add_matrix() for i in range(rows_cols)]
symbol = input()
[find_symbol(i) for i in range(len(matrix))]

print(f'{symbol} does not occur in the matrix')